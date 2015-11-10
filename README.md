#Python
---

##v1.2更细说明
1. 修复了媒体信息模块

##v1.1更新说明
1. 修复了硬件相关API无法使用的BUG
2. 生成二维码需要PIL,qrcode模块

##v1.0更新说明
1. 添加了对消息、推送事件的处理
2. 添加了模拟服务号token的操作
3. 添加了一个django版的DEMO

##微信公众平台第三方Python SDK
Github地址：https://github.com/jxtech/wechatpy

文档地址：http://wechatpy.readthedocs.org/zh_CN/latest/

##环境需求

pycrypto >= 2.6.1 :$pip install pycrypto>=2.6.1

wechatpy :$pip install wechatpy

PIL:pip install PIL(非必需，仅在生成二维码处用到)

qrcode:pip install qrcode(非必需，仅在生成二维码处用到)

##DEMO使用说明

1. 请补充如下信息：
	1. APP_ID,APP_SECRET,TOKEN(wrist/wechat/tools.py)
	2. 数据库信息(wrist/wrist/settings.py)
2. wrist/wechat/server.py下为各消息、推送事件的处理，大家请自行修改为自己的处理
3. wrist/wechat/tools.py下为主动调用的API，详细信息见“手环相关API”
4. 用于微信测试号：在本机部署好Django项目，使其能通过80端口访问(通过Nginx、Apache转发或者直接runserver 0.0.0.0:80)，微信测试号那里的URL填写:http://你的ip或者域名/wechat/   例：http://*.*.*.*/wechat/
5. 注意：通过getOpenId获得的openId是关注海思力服务号的openId，而不是测试号的openId(同一用户对于不同公众号来说有不同的openId）。测试号的OpenId可在测试号页面查看，也可自行记录在数据库中以便使用。openId的获得可通过msg.source(msg为wrist/wechat/server.py的那个msg)

##手环相关API

注：请先在开头出填写APP_ID,APP_SECRET。使用方法即import tools

####transMsg

函数功能：

向设备发送信息

参数：transMsg(deviceType, deviceId, user, content)

#### createQrByDeviceId

函数功能：

直接由deviceId生成相应的二维码图片

参数：createQrByDeviceId(deviceId)

#### getStat

函数功能：

查询设备状态

参数：getStat(deviceId)

返回结果：

一个JSON数组，例如:

	{"errcode":0,"errmsg":"ok","status":1,"status_info":"authorized"}

#### getOpenId

函数功能：

查询设备绑定的用户的OpenId

参数：getOpenId(deviceType, deviceId)

返回结果：

一个JSON数组，例如：

	{
	"open_id":["omN7ljrpaxQgK4NW4H5cRzFRtfa8","omN7ljtqrTZuvYLkjPEX_t_Pmmlg",],
	"resp_msg":{"ret_code":0,"error_info":"get open id list OK!"}
	}

##微信相关API

#### customSendText

函数功能：

给用户发送客服文本信息

参数：customSendText(user, content)

user：目标用户的openId,可通过msg.source获得

#### uploadMedia

函数功能：

上传临时素材

参数：uploadMedia(type, filename)

type:"image","voice","video","thumb"

filename:本地文件名，默认目录在项目文件夹下(即与manage.py同级)

注：返回信息为一个JSON数组，若返回成功，在["media_id"]中获得media_id以便发送其他信息时使用。临时素材只保留3天

#### customSendImage

函数功能：

给用户发送客服图片信息

参数：customSendImage(user, filename, mediaId=None)

注：可直接传入filename使用，也可传入之前uploadMedia得到的mediaID使用。建议传入mediaID

#### customSendVoice/customSendVideo

函数功能：

给用户发送客服声音/视频信息

参数：customSendVideo/customSendVoice(user, mediaId)

#### customSendArticle/customSendArticles

函数功能：

给用户发送客服文章信息

参数：customSendArticle(user, title, description, image, url) / customSendArticles(user, articles)

title,description: 文章的标题和概述

image:图片的url地址

url:点击后的链接地址

articles:多个article的数组(每个article是一个dict)

#### menuCreate

函数功能:

创建自定义菜单

参数：menuCreate(body)

body:JSON字符串，格式如下： 详细格式要求可查看微信官方文档

	{
	 "button":[
	 {	
	      "type":"click",
	      "name":"今日歌曲",
	      "key":"V1001_TODAY_MUSIC"
	  },
	  {
	       "name":"菜单",
	       "sub_button":[
	       {	
	           "type":"view",
	           "name":"搜索",
	           "url":"http://www.soso.com/"
	        },
	        {
	           "type":"view",
	           "name":"视频",
	           "url":"http://v.qq.com/"
	        },
	        {
	           "type":"click",
	           "name":"赞一下我们",
	           "key":"V1001_GOOD"
	        }]
	   }]
	}

注：创建自定义菜单时会自动删除原有菜单

#### menuQuery()

函数功能：

查看自定义菜单

参数：menuQuery()

返回值：

一个JSON字符串，例子如下：

    {"menu":
		{"button":[
			{"type":"click","name":"今日歌曲","key":"V1001_TODAY_MUSIC","sub_button":[]},
			{"type":"click","name":"歌手简介","key":"V1001_TODAY_SINGER","sub_button":[]},
			{"name":"菜单","sub_button":[
				{"type":"view","name":"搜索","url":"http://www.soso.com/","sub_button":[]},
				{"type":"view","name":"视频","url":"http://v.qq.com/","sub_button":[]},
				{"type":"click","name":"赞一下我们","key":"V1001_GOOD","sub_button":[]}
			]}
		]}
	}

#### menuDelete

函数功能：

删除原有自定义菜单

参数：menuDelete()

返回值：

一个JSON字符串，表示操作结果，如下：

	{"errcode":0,"errmsg":"ok"}

