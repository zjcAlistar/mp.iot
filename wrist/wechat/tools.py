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

APP_ID = "wx87b3855d89436d96"
APP_SECRET = "4d68e68b7f53bc0c78752605b0dab364"
TOKEN = "chendaxixi"
client = WeChatClient(APP_ID, APP_SECRET)
DEVICE_BASE_URL = 'https://api.weixin.qq.com/device/'
MEDIA_BASE_URL = "https://api.weixin.qq.com/cgi-bin/media/"
tmp_media_id = None

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

def POST(url, foot, data, params, files=None):
    tmp = "access_token=%s" % params["access_token"]
    for item in params:
        if not item == "access_token":
            tmp += "&%s=%s" % (item, params[item]) 
    res = requests.request(method="post", url="%s%s?%s" % (url, foot, tmp), 
       data=data, files=files)
    res.encoding = 'utf-8'
    return res.json()    

def uploadMedia(type, filename):
    res = POST(MEDIA_BASE_URL, "upload", {"media": file(filename)}, {"access_token": client.fetch_access_token()["access_token"], "type": type}, {filename:(filename,open(filename,'rb'))})   
    return res

def customSendText(user, content):
    return client.message.send_text(user, content)

def customSendImage(user, filename, mediaId=None):
    if mediaId:
        return client.message.send_image(user, mediaId)
    res =  updateMedia("image", filename)
    try:
        return client.message.send_image(user, res["media_id"])
    except:
        return res

def customSendVoice(user, mediaId):
    return client.message.send_voice(user, mediaId)

def customSendVideo(user, mediaId, title=None, description=None):
    return client.message.send_video(user, mediaId, title, description)

def customSendArticle(user, title, description, image, url):
    return client.message.send_articles(user, [{"title":title,"description":description,"image":image,"url":url}])

def customSendArticles(user, articles):
    return client.message.send_articles(user, articles)

def getStat(deviceId):
    return POST(DEVICE_BASE_URL, "get_stat", {"device_id":deviceId}, {"access_token": getToken()})

def getOpenId(deviceType, deviceId):
    return POST(DEVICE_BASE_URL, "get_openid", {"device_type":deviceType,"device_id":deviceId}, {"access_token": getToken()})
   
def transMsg(deviceType, deviceId, user, content):
    content = to_text(base64.b64encode(to_binary(content)))
    return POST(DEVICE_BASE_URL, "transmsg", {"device_type":deviceType,"device_id":deviceId,"openid":user,"content":content}, {"access_token": getToken()})

def createQrByDeviceId(deviceId, filename):
    res = POST(DEVICE_BASE_URL, "create_qrcode", json.dumps({"device_num": 1, "device_id_list":[deviceId]}), {"access_token": getToken()})
    try:
        ticket = res["code_list"][0]["ticket"]
        img = qrcode.make(ticket)
        img.save(filename)
        return ticket
    except:
        return res

if __name__ == "__main__":
    print "python-wechat tools modified by chendaxixi"   
