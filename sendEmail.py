#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.MIMEText import MIMEText
from email.Header import Header


# 第三方 SMTP 服务
mail_host="smtp.startimes.com.cn"  #设置服务器
mail_user="12345@qq.com"    #用户名
mail_pass="12345"   #口令 


sender = '12345@qq.com'
receivers = ['12345@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
#创建一个带附件的实例
message = MIMEMultipart()
#message['From'] = Header("StarTimes", 'utf-8')
message['To'] =  Header("12345@qq.com")
subject = 'test'
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
message.attach(MIMEText('''Hi,
test!!!.
''', 'plain', 'utf-8'))

filename1='test-'+date1+'.xls'
date1=(datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y%m%d')

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open(filename1, 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename='+filename1
message.attach(att1)
 

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
    smtpObj.quit()
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
    smtpObj.quit()
