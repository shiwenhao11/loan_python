#encoding:utf-8

import smtplib
import email.mime.multipart
import email.mime.text
import email.mime.image
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#定义收件人
to_list='fenghua@nonobank.com','shiwenhao@nonobank.com','luyue@nonobank.com','suzhiyu@nonobank.com','songqi@nonobank.com','goujingwei@nonobank.com'


#配置邮箱信息
msg = email.mime.multipart.MIMEMultipart()
msg['subject'] = '贷款组测试报告'             #邮件主题

#查找当前目录下html文件
def endWith(s, *endstring):                 #定义查询方法
    array = map(s.endswith, endstring)
    if True in array:
        return True
    else:
        return False
if __name__ == '__main__':
    import os

    s = os.listdir('./output')             #查找文件目录
    f_file = []
    for i in s:
        if endWith(i, '.html'):
            print ("找到文件"+i)            #查找到文件并打印
#读取文件并复制
html=open('./output/'+i).read()            #读取文件目录默认为根目录
#构造邮件内容
part2 = MIMEText(html, 'html','utf-8')
msg.attach(part2)

#构造附件
att = MIMEText(open('./output/'+i, 'rb').read(), 'base64', 'utf-8')    #上传附件目录，默认为根目录
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)



#发送邮件
smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('mail.nonobank.com')          # 邮箱smtp地址
smtp.login('shiwenhao', 'Swh1314521')      #发件人邮箱账号密码
smtp.sendmail('shiwenhao@nonobank.com', to_list, msg.as_string())   #发件人收件人
smtp.quit()
