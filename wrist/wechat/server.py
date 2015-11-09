
#-*- coding=utf-8 -*-
###
# description: 微信公众号被动回复服务
###

__author__ = "chendaxixi"

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from wechat import tools
from wechatpy import parse_message, create_reply

@csrf_exempt
def handle(request):
    if request.method == "GET":
        if not tools.checkSignature(request):
            return HttpResponse("invalid signature")
        else:
            return HttpResponse(request.GET["echostr"]) 
    msg = parse_message(request.body)
    return msg_splitter[msg.type](msg)

#对文本信息进行回复
def textHandle(msg):
    return HttpResponse(create_reply("Hello World!I am text", message=msg))

#对语音信息进行回复
def voiceHandle(msg):
    return HttpResponse(create_reply("Hello World!I am voice", message=msg))

#对图片信息进行回复
def imageHandle(msg):
    return HttpResponse(create_reply("Hello World!I am image", message=msg))

#对视频信息进行回复
def videoHandle(msg):
    return HttpResponse(create_reply("Hello World!I am video", message=msg))

#对地理位置信息进行回复
def locationHandle(msg):
    return HttpResponse(create_reply("Hello World!I am location", message=msg))

#对链接信息进行回复
def linkHandle(msg):
    return HttpResponse(create_reply("Hello World!I am link", message=msg))

#对小视频信息进行回复
def svHandle(msg):
    return HttpResponse(create_reply("Hello World!I am short video", message=msg))

#对事件信息进行处理
def eventHandle(msg):
    return event_splitter[msg.event](msg)

#用户关注事件
def subEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 用户关注事件", message=msg))

#对用户取消关注事件
def unsubEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 用户取关事件", message=msg))

#未关注用户扫描带参数二维码事件
def subscanEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 未关注用户扫描带参数二维码事件", message=msg))

#已关注用户扫描带参数二维码事件
def scanEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 已关注用户扫描带参数二维码事件", message=msg))

#上报地理位置事件
def locationEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 上报地理位置事件", message=msg))

#点击菜单拉取消息事件
def clickEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单拉取消息事件", message=msg))

#点击菜单跳转链接事件
def viewEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单跳转链接事件", message=msg))

#群发消息发送任务完成事件
def masssendEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 群发消息发送任务完成事件", message=msg))

#模板消息发送任务完成事件
def templatesendEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 模板消息发送任务完成事件", message=msg))

#扫码推事件
def sc_pushEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 扫码推事件", message=msg))

#扫码推事件且弹出“消息接收中”提示框
def sc_waitEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 扫码推事件且弹出“消息接收中”提示框", message=msg))

#弹出系统拍照发图事件
def pic_photo_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出系统拍照发图事件", message=msg))

#弹出拍照或者相册发图事件
def pic_photo_album_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出拍照或者相册发图事件", message=msg))

#弹出微信相册发图器事件
def pic_wechat_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出微信相册发图器事件", message=msg))

#弹出地理位置选择器事件
def select_location_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出地理位置选择器事件", message=msg))

msg_splitter = {
  "text": textHandle,
  "voice": voiceHandle,
  "image": imageHandle,
  "video": videoHandle,
  "location": locationHandle,
  "link": linkHandle,
  "shortvideo": svHandle,
  "event": eventHandle,
}

event_splitter = {
  "subscribe": subEvent,
  "unsubscribe": unsubEvent,
  "subscribe_scan": subscanEvent,
  "scan": scanEvent,
  "location": locationEvent,
  "click": clickEvent,
  "view": viewEvent,
  "masssendjobfinish": masssendEvent,
  "templatesendjobfinish": templatesendEvent,
  "scancode_push": sc_pushEvent,
  "scancode_waitmsg": sc_waitEvent,
  "pic_sysphoto": pic_photo_Event,
  "pic_photo_or_album": pic_photo_album_Event,
  "pic_weixin": pic_wechat_Event,
  "location_select": select_location_Event,
}
