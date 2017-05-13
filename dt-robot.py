#!/usr/bin/env python
#coding=utf-8

"""
钉钉群自定义机器人
author：疯狂的技术宅
github：https://github.com/magician000

学习python时做的练习，纯粹为了娱乐
如果存在bug请自行修改，不提供任何支持

官方文档
https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.z5MWoh&treeId=257&articleId=105735&docType=1

这个接口的消息格式命名风格不统一，坑爹呢？
所以不要迷信大公司就怎样规范。
"""

import sys
import urllib2
import urllib
import json
import time

#自定义机器人的封装类
class DtalkRobot(object):
	"""docstring for DtRobot"""
	webhook = ""
	def __init__(self, webhook):
		super(DtalkRobot, self).__init__()
		self.webhook = webhook

	#text类型
	def sendText(self, msg, isAtAll=False, atMobiles=[]):
		data = {"msgtype":"text","text":{"content":msg},"at":{"atMobiles":atMobiles,"isAtAll":isAtAll}}
		return self.post(data)

	#markdown类型
	def sendMarkdown(self, title, text):
		data = {"msgtype":"markdown","markdown":{"title":title,"text":text}}
		return self.post(data)

	#link类型
	def sendLink(self, title, text, messageUrl, picUrl=""):
		data = {"msgtype": "link","link": {"text": text, "title":title,"picUrl": picUrl,"messageUrl": messageUrl}}
		return self.post(data)

	#ActionCard类型
	def sendActionCard(self, actionCard):
		data = actionCard.getData();
		return self.post(data)

	#FeedCard类型
	def sendFeedCard(self, links):
		data = {"feedCard":{"links":links},"msgtype":"feedCard"}
		return self.post(data)

	def post(self, data):
		post_data = json.JSONEncoder().encode(data)
 		print post_data
		req = urllib2.Request(webhook, post_data)
 		req.add_header('Content-Type', 'application/json')
		content = urllib2.urlopen(req).read()
		return content

#ActionCard类型消息结构
class ActionCard(object):
	"""docstring for ActionCard"""
	title = ""
	text = ""
	singleTitle = ""
	singleURL = ""
	btnOrientation = 0
	hideAvatar = 0
	btns = []

	def __init__(self, arg=""):
		super(ActionCard, self).__init__()
		self.arg = arg

	def putBtn(self, title, actionURL):
		self.btns.append({"title":title,"actionURL":actionURL})

	def getData(self):
		data = {"actionCard":{"title":self.title,"text":self.text,"hideAvatar":self.hideAvatar,"btnOrientation":self.btnOrientation,"singleTitle":self.singleTitle,"singleURL":self.singleURL,"btns":self.btns},"msgtype":"actionCard"}
		return data
		
#FeedCard类型消息格式
class FeedLink(object):
	"""docstring for FeedLink"""
	title = ""
	picUrl = ""
	messageUrl = ""

	def __init__(self, arg=""):
		super(FeedLink, self).__init__()
		self.arg = arg
		
	def getData(self):
		data = {"title":self.title,"picURL":self.picUrl,"messageURL":self.messageUrl}
		return data
		

#测试
webhook = "https://oapi.dingtalk.com/robot/send?access_token=改成你自己的token"
if __name__ == "__main__":

    robot = DtalkRobot(webhook)

    print robot.sendText( "现在时间：["+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"]", False, ["13912345678 "])
    print robot.sendLink("link类型", "link类型内容link类型内容link类型内容link类型内容link类型内容link类型内容link类型内容", "http://www.baidu.com","http://scimg.jb51.net/allimg/160716/103-160G61012361X.jpg")
    print robot.sendMarkdown("markdown类型", "## 标题2 \n##### 标题3 \n* 第一 \n* 第二 \n\n[链接](http://www.baidu.com/) \n")
    
    ########
    link1 = FeedLink()
    link1.title = "我的github"
    link1.picUrl = "https://avatars0.githubusercontent.com/u/3347358?v=3&u=318d72d3ec999cfe4c7f37765c9c1f92df79ab1c&s=400"
    link1.messageUrl = "https://github.com/magician000"
    link2 = FeedLink()
    link2.title = "github官网"
    link2.picUrl = "https://avatars0.githubusercontent.com/u/18586086?v=3&u=e6187b04ba02e3861ad4acccc5a1f1f5d46d40a0&s=400"
    link2.messageUrl = "https://www.github.com/"
    feeds = [link1.getData(), link2.getData()]
    
    print robot.sendFeedCard(feeds)

    #ActionCard类型，两种跳转规则的设置见官方文档
    #整体跳转ActionCard类型
    ac = ActionCard();
    ac.title = "整体跳转ActionCard类型"
    ac.text = "#### 整体跳转ActionCard类型 \n\n![TTTT](https://avatars0.githubusercontent.com/u/3347358?v=3&u=318d72d3ec999cfe4c7f37765c9c1f92df79ab1c&s=400) \n>整体\n跳转\nActionCard类型\n"
    ac.singleTitle = "查看全文"
    ac.singleURL = "https://github.com/magician000"
    print robot.sendActionCard(ac)
    ########
    #独立跳转ActionCard类型
    ac = ActionCard();
    ac.title = "独立跳转ActionCard类型"
    ac.text = "#### 独立跳转ActionCard类型 \n\n![TTTT](https://avatars0.githubusercontent.com/u/18586086?v=3&u=e6187b04ba02e3861ad4acccc5a1f1f5d46d40a0&s=400) \n>独立\n跳转\nActionCard类型\n"
    ac.btnOrientation = 1
    ac.putBtn("github", "https://github.com/magician000")
    ac.putBtn("脑洞空间", "https://github.com/mind-boggling")
    ac.singleTitle = ""
    ac.singleURL = ""
    print robot.sendActionCard(ac)

