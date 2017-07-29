#coding=utf-8
import random



#构建环境类stb
#create by luyue
class stb_url():
    loan = ''
    mkt = ''
    pay = ''
    usr = ''
    trd = ''
    invt = ''
    prod = ''


#随机生成一个手机号
#create by luyue
def create_mobile_num():
    mobile_num = random.choice(['139','138','185','136','158','159'])+"".join(random.choice("0123456789") for i in range(8))
    return mobile_num







