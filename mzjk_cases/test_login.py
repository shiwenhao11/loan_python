#coding=utf-8
import simplejson

from bizapi.usr_biz_api import *



def test_user_register():
    res = usr_api_doRegister()
    hjson = simplejson.loads(res)
    print res
    print hjson['errorMessage']
    assert hjson['errorMessage'] == '成功'
    assert hjson['succeed'] == True
    res2 = usr_api_doRegister()
    print res2
    hjson = simplejson.loads(res2)
    assert hjson['errorMessage'] == '错误'
