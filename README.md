## 微信硬件接入
---

###接入流程

1.	针对个人开发者/测试用户，申请微信公众平台测试账号 http://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login
2.	开启设备接口
3.	选择你喜欢的后台语言，从对应分支下载Demo
4.	根据分支对应的README.md配置环境，将Demo部署到自己的服务器上
5.	在微信测试号/服务号的开发者中心处填写接口配置信息
6.	扫描设备二维码，将自己的微信账号与设备绑定

###通信流程

1.	点击菜单/定时触发，调用API发送HTTP请求(此时得到微信服务器是否发送成功的response)
2.	服务器url收到携带XML结构体的HTTP请求，并返回XML结构体

###Bong手环数据获取

相关API将公布在Data_Bong分支