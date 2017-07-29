#coding=utf-8

import simplejson
import urllib2

from utils.base_tools import *
from config.config_env import *




def usr_api_doRegister():

    mobile_num = create_mobile_num()
    url = config_url.usr + 'usr/register/doRegister'

    post_data = simplejson.dumps({
    "passWord": "",
    "imgKey": "",
    "adPlan": "",
    "referer": "",
    "bizCode": "mzjk",
    "openId": "",
    "registerType": "FASTM",
    "registerApproach": "1",
    "deviceId": "",
    "channelDetail": "",
    "advisor": "",
    "inviteMobile": "",
    "clientType": "pc",
    "pcId": "1",
    "channelId": "",
    "mobileCode": "888888",
    "tokenId": "",
    "landingPage": "",
    "ip": "192.168.1.111",
    "mobile": mobile_num,
    "adUnit": "",
    "csUserType": "1",
    "imgCode": "",
    "mobileKey": mobile_num,
    "userName": "",
    "approach9": "",
    "approach8": "",
    "approach5": "",
    "approach4": "",
    "approach7": "",
    "blackBox": "1",
    "approach6": "",
    "inviteCode": "",
    "approach10": "",
    "userType": "2",
    "operation": ""
    })
    #发送post请求
    Response  = urllib2.Request(url, post_data, {'Content-Type':'application/json'})
    f = urllib2.urlopen(Response)
    Res = f.read()
    f.close()

    return Res

