#coding=utf-8
import random
import urllib2
import simplejson


#随机生成一个手机号
#create by luyue
def create_mobile_num():
    mobile_num = random.choice(['139','138','185','136','158','159'])+"".join(random.choice("0123456789") for i in range(8))
    return mobile_num


def host(name):
    loan1 = 'http://192.168.3.185:8081/loan-app/'
    mkt1 = 'http://192.168.3.185:8082/mkt-app/'
    pay1 = 'http://192.168.3.185:8083/pay-app/'
    usr1 = 'http://192.168.3.185:8085/usr-app/'
    acc1 = 'http://192.168.3.159:8080/acc-app/'
    trd1 = 'http://192.168.3.159:8084/trd-app/'
    invt1 = 'http://192.168.3.159:8082/invt-app/'
    prod1 = 'http://192.168.3.159:8083/prod-app/'

    loan2 = 'http://192.168.3.86:8081/loan-app/'
    mkt2 = 'http://192.168.3.86:8082/mkt-app/'
    pay2 = 'http://192.168.3.86:8083/pay-app/'
    usr2 = 'http://192.168.3.86:8085/usr-app/'
    acc2 = 'http://192.168.3.35:8080/acc-app/'
    trd2 = 'http://192.168.3.35:8084/trd-app/'
    invt2 = 'http://192.168.3.35:8082/invt-app/'
    prod2 = 'http://192.168.3.35:8083/prod-app/'

    loan3 = 'http://192.168.3.197:8081/loan-app/'
    mkt3 = 'http://192.168.3.197:8082/mkt-app/'
    pay3 = 'http://192.168.3.197:8083/pay-app/'
    usr3 = 'http://192.168.3.197:8085/usr-app/'
    acc3 = 'http://192.168.3.196:8080/acc-app/'
    trd3 = 'http://192.168.3.196:8084/trd-app/'
    invt3 = 'http://192.168.3.196:8082/invt-app/'
    prod3 = 'http://192.168.3.196:8083/prod-app/'

    loan4 = 'http://192.168.3.176:8081/loan-app/'
    mkt4 = 'http://192.168.3.176:8082/mkt-app/'
    pay4 = 'http://192.168.3.176:8083/pay-app/'
    usr4 = 'http://192.168.3.176:8085/usr-app/'
    acc4 = 'http://192.168.3.175:8080/acc-app/'
    trd4 = 'http://192.168.3.175:8084/trd-app/'
    invt4 = 'http://192.168.3.175:8082/invt-app/'
    prod4 = 'http://192.168.3.175:8083/prod-app/'

    loan5 = 'http://192.168.3.81:8081/loan-app/'
    mkt5 = 'http://192.168.3.81:8082/mkt-app/'
    pay5 = 'http://192.168.3.81:8083/pay-app/'
    usr5 = 'http://192.168.3.81:8085/usr-app/'
    acc5 = 'http://192.168.3.80:8080/acc-app/'
    trd5 = 'http://192.168.3.80:8084/trd-app/'
    invt5 = 'http://192.168.3.80:8082/invt-app/'
    prod5 = 'http://192.168.3.80:8083/prod-app/'

    loan6 = 'http://192.168.3.157:8081/loan-app/'
    mkt6 = 'http://192.168.3.157:8082/mkt-app/'
    pay6 = 'http://192.168.3.157:8083/pay-app/'
    usr6 = 'http://192.168.3.157:8085/usr-app/'
    acc6 = 'http://192.168.3.173:8080/acc-app/'
    trd6 = 'http://192.168.3.173:8084/trd-app/'
    invt6 = 'http://192.168.3.173:8082/invt-app/'
    prod6 = 'http://192.168.3.173:8083/prod-app/'

    loan7 = 'http://192.168.3.33:8081/loan-app/'
    mkt7 = 'http://192.168.3.33:8082/mkt-app/'
    pay7 = 'http://192.168.3.33:8083/pay-app/'
    usr7 = 'http://192.168.3.33:8085/usr-app/'
    acc7 = 'http://192.168.3.32:8080/acc-app/'
    trd7 = 'http://192.168.3.32:8084/trd-app/'
    invt7 = 'http://192.168.3.32:8082/invt-app/'
    prod7 = 'http://192.168.3.32:8083/prod-app/'

    loan8 = 'http://192.168.3.49:8081/loan-app/'
    mkt8 = 'http://192.168.3.49:8082/mkt-app/'
    pay8 = 'http://192.168.3.49:8083/pay-app/'
    usr8 = 'http://192.168.3.49:8085/usr-app/'
    acc8 = 'http://192.168.3.48:8080/acc-app/'
    trd8 = 'http://192.168.3.48:8084/trd-app/'
    invt8 = 'http://192.168.3.48:8082/invt-app/'
    prod8 = 'http://192.168.3.48:8083/prod-app/'

    if name == 'stb1_loan':
        return loan1
    elif name == 'stb1_mkt':
        return mkt1
    elif name == 'stb1_pay':
        return pay1
    elif name == 'stb1_usr':
        return usr1
    elif name == 'stb1_acc':
        return acc1
    elif name == 'stb1_trd':
        return trd1
    elif name == 'stb1_invt':
        return invt1
    elif name == 'stb1_prod':
        return prod1

    elif name == 'stb2_loan':
        return loan2
    elif name == 'stb2_mkt':
        return mkt2
    elif name == 'stb2_pay':
        return pay2
    elif name == 'stb2_usr':
        return usr2
    elif name == 'stb2_acc':
        return acc2
    elif name == 'stb2_trd':
        return trd2
    elif name == 'stb2_invt':
        return invt2
    elif name == 'stb2_prod':
        return prod2

    elif name == 'stb3_loan':
        return loan3
    elif name == 'stb3_mkt':
        return mkt3
    elif name == 'stb3_pay':
        return pay3
    elif name == 'stb3_usr':
        return usr3
    elif name == 'stb3_acc':
        return acc3
    elif name == 'stb3_trd':
        return trd3
    elif name == 'stb3_invt':
        return invt3
    elif name == 'stb3_prod':
        return prod3

    elif name == 'stb4_loan':
        return loan4
    elif name == 'stb4_mkt':
        return mkt4
    elif name == 'stb4_pay':
        return pay4
    elif name == 'stb4_usr':
        return usr4
    elif name == 'stb4_acc':
        return acc4
    elif name == 'stb4_trd':
        return trd4
    elif name == 'stb4_invt':
        return invt4
    elif name == 'stb4_prod':
        return prod4

    elif name == 'stb5_loan':
        return loan5
    elif name == 'stb5_mkt':
        return mkt5
    elif name == 'stb5_pay':
        return pay5
    elif name == 'stb5_usr':
        return usr5
    elif name == 'stb5_acc':
        return acc5
    elif name == 'stb5_trd':
        return trd5
    elif name == 'stb5_invt':
        return invt5
    elif name == 'stb5_prod':
        return prod5

    elif name == 'stb6_loan':
        return loan6
    elif name == 'stb6_mkt':
        return mkt6
    elif name == 'stb6_pay':
        return pay6
    elif name == 'stb6_usr':
        return usr6
    elif name == 'stb6_acc':
        return acc6
    elif name == 'stb6_trd':
        return trd6
    elif name == 'stb6_invt':
        return invt6
    elif name == 'stb6_prod':
        return prod6

    elif name == 'stb7_loan':
        return loan7
    elif name == 'stb7_mkt':
        return mkt7
    elif name == 'stb7_pay':
        return pay7
    elif name == 'stb7_usr':
        return usr7
    elif name == 'stb7_acc':
        return acc7
    elif name == 'stb7_trd':
        return trd7
    elif name == 'stb7_invt':
        return invt7
    elif name == 'stb7_prod':
        return prod7

    elif name == 'stb8_loan':
        return loan8
    elif name == 'stb8_mkt':
        return mkt8
    elif name == 'stb8_pay':
        return pay8
    elif name == 'stb8_usr':
        return usr8
    elif name == 'stb8_acc':
        return acc8
    elif name == 'stb8_trd':
        return trd8
    elif name == 'stb8_invt':
        return invt8
    elif name == 'stb8_prod':
        return prod8
    else:
        print (str(name) + "环境配置不存在，请确认下")

print host('stb4_loan')


