#-*- coding=utf-8 -*-
###
# description: 微信API
###

__author__ = "chendaxixi"

import hashlib
import httplib
from wechatpy.client import WeChatClient

APP_ID = ""
APP_SECRET = ""
TOKEN = ""
client = WeChatClient(APP_ID, APP_SECRET)

def checkSignature(request):
    try:
        sign = request.GET["signature"]
        timestamp = request.GET["timestamp"]
        nonce = request.GET["nonce"]
    except:
        return False

    token = TOKEN
    tmp = [timestamp, nonce, token]
    tmp.sort()
    res = tmp[0] + tmp[1] + tmp[2]
    m = hashlib.sha1(res)
    return m.hexdigest() == sign

def getToken():
    conn = httplib.HTTPConnection("wx.chendaxixi.me")
    conn.request("GET", "/token")
    return conn.getresponse().read()    

def menuCreate(body):
    client.menu.delete()
    return client.menu.create(body)

def menuQuery():
    return client.menu.get()

def menuDelete():
    return client.menu.delete()

def customSendText(user, content):
    return client.message.send_text(user, content)

def customSendImage(user, filename):
    f = open(filename)
    res =  client.media.upload("image", f)
    f.close()
    data = json.loads(res)
    try:
        return client.message.send_image(user, data["media_id"])
    except:
        return res

def getStat(deviceId):
    _client = WeChatClient(APP_ID, APP_SECRET, getToken())
    return _client.device.get_stat(deviceId)

def getOpenId(deviceType, deviceId):
    _client = WeChatClient(APP_ID, APP_SECRET, getToken())
    return _client.device.get_user_id(deviceType, deviceId)
   
def transMsg(deviceType, deviceId, user, content):
    _client = WeChatClient(APP_ID, APP_SECRET, getToken())
    return _client.device.send_message(deviceType, deviceId, user, content)

def createQrByDeviceId(deviceId):
    _client = WeChatClient(APP_ID, APP_SECRET, getToken())
    res = _client.device.create_qrcode([deviceId])
    try:
        ticket = json.loads(res)["code_list"][0]["ticket"]
        #TODO
        return ticket
    except:
        return res

if __name__ == "__main__":
    print "python-wechat tools modified by chendaxixi"   
