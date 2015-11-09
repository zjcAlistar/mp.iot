#Python
---

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

##DEMO使用说明

1. 请补充如下信息：
	1. APP_ID,APP_SECRET,TOKEN(wrist/wechat/tools.py)
	2. 数据库信息(wrist/wrist/settings.py)
2. wrist/wechat/server.py下为各消息、推送事件的处理，默认版本为回复一个文本"Hello World！I am **." 大家请自行修改为自己的处理
3. wrist/wechat/tools.py下为主动调用的API，详细信息见“手环相关API”

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

一个JSON字符串，例如:

	{"errcode":0,"errmsg":"ok","status":1,"status_info":"authorized"}

#### getOpenId

函数功能：

查询设备绑定的用户的OpenId

参数：getOpenId(deviceType, deviceId)

返回结果：

一个JSON字符串，例如：

	{
	"open_id":["omN7ljrpaxQgK4NW4H5cRzFRtfa8","omN7ljtqrTZuvYLkjPEX_t_Pmmlg",],
	"resp_msg":{"ret_code":0,"error_info":"get open id list OK!"}
	}

#### customSendText

函数功能：

给用户发送客服文本信息

参数：customSendText(user, content)

user：目标用户的openId,可通过boundInfo获得

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

