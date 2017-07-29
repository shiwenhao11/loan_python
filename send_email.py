#coding=utf-8

import smtplib
import email.mime
import email.mime.multipart
import email.mime.text
import email.mime.image

from email.mime.text import MIMEText
from email.mime.image import MIMEImage


#发送邮件email功能
#create by shiwenhao
# 配置邮箱信息
msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'luyue15@163.com'  # 发件人邮箱
msg['to'] = '623160761@qq.com'  # 收件人邮箱
msg['subject'] = '贷款组测试报告'  # 邮件主题
# 读取文件并复制
html = open('./output/test_report.html').read()
# 构造邮件内容
part2 = MIMEText(html, 'html', 'utf-8')
msg.attach(part2)

# 构造附件
att = MIMEText(open('./output/test_report.html', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)

# 发送邮件
smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.139.com')  # 使用的发送者邮箱的那啥来着，post
smtp.login('18237850395', 'it789123')
smtp.sendmail('18237850395@139.com', '623160761@qq.com', str(msg))
smtp.quit()


