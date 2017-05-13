# DingTalkRobot-python
钉钉群自定义机器人webhook协议的Python封装

学习python的练习，纯粹为了娱乐，如果存在bug请自行修改，不提供任何支持。

有问题请查阅[钉钉的官方文档](https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.z5MWoh&treeId=257&articleId=105735&docType=1)

#使用方法
```python
webhook = "https://oapi.dingtalk.com/robot/send?access_token=your_token"
robot = DtalkRobot(webhook)
robot.sendMarkdown("消息title", "Markdown格式的内容")
```
