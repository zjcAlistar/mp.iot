#-*- coding=utf-8 -*-
###
# description: 微信API
###

__author__ = "chendaxixi"

import hashlib
import httplib
import requests
import base64
import json
import qrcode
from wechatpy.utils import to_text, to_binary
from wechatpy.client import WeChatClient

APP_ID = ""
APP_SECRET = ""
TOKEN = ""
client = WeChatClient(APP_ID, APP_SECRET)
API_BASE_URL = 'https://api.weixin.qq.com/device/'

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

def deviceAPI(url, data):
    res = requests.request(method="post", url="%s%s?access_token=%s" % (API_BASE_URL, url, getToken()), 
       data=data)
    res.encoding = 'utf-8'
    try:
        res = res.json()
    except:
        res = res
    return res    

def getStat(deviceId):
    return deviceAPI("get_stat", {"device_id":deviceId})

def getOpenId(deviceType, deviceId):
    return deviceAPI("get_openid", {"device_type":deviceType,"device_id":deviceId})
   
def transMsg(deviceType, deviceId, user, content):
    content = to_text(base64.b64encode(to_binary(content)))
    return deviceAPI("transmsg", {"device_type":deviceType,"device_id":deviceId,"openid":user,"content":content})

def createQrByDeviceId(deviceId, filename):
    res = deviceAPI("create_qrcode", json.dumps({"device_num": 1, "device_id_list":[deviceId]}))
    try:
        ticket = res["code_list"][0]["ticket"]
        img = qrcode.make(ticket)
        img.save(filename)
        return ticket
    except:
        return res

if __name__ == "__main__":
    print "python-wechat tools modified by chendaxixi"   
