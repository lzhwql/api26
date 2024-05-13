#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2024/4/27 9:14
# Author     : smart
# @File      : send_email_base.py
# @Software  : PyCharm
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('邮件的内容','plain','utf-8')
msg['From'] = '1705158296@qq.com'
msg['To'] = '1705158296@qq.com'
msg['Subject'] = '邮件标题'
smtp = smtplib.SMTP_SSL("smtp.qq.com")
smtp.login('1705158296@qq.com','epgyuewydtumbehd')
smtp.sendmail('1705158296@qq.com','1705158296@qq.com',msg.as_string())
smtp.quit()