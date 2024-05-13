#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2024/4/27 9:48
# Author     : smart
# @File      : send_email_alt.py
# @Software  : PyCharm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
with open("report.html",encoding='utf-8') as f:
    email_body = f.read()
# msg = MIMEText('邮件的内容','plain','utf-8')
msg = MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf-8'))
msg['From'] = '1705158296@qq.com'
msg['To'] = '1705158296@qq.com'
msg['Subject'] = Header('接口测试报告','utf-8')
att1 = MIMEText(open("report.html","rb").read(),'base64','utf-8')
att1["Content_Type"] = 'application/octet-stream'
att1["Content_Disposition"] = 'attachment;filename="report.html"'
msg.attach(att1)
smtp = smtplib.SMTP_SSL("smtp.qq.com")
smtp.login('1705158296@qq.com','epgyuewydtumbehd')
smtp.sendmail('1705158296@qq.com','1705158296@qq.com',msg.as_string())
smtp.quit()