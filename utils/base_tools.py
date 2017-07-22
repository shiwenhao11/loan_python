import random
import urllib2
import simplejson


#随机生成一个手机号
#create by luyue
def create_mobile_num():
    mobile_num = random.choice(['139','138','185','136','158','159'])+"".join(random.choice("0123456789") for i in range(8))
    return mobile_num
