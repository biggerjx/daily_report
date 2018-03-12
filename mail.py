# -*- coding: utf-8-*-

'''

author ：yanjx
功能：用于发送邮件
状态：已完成

'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '843305474@qq.com'
password = 'wspzwudnvvnkbcjf'
to_addr = '3468320743@qq.com'
smtp_server = 'smtp.qq.com'

##############################################
#1、发送内容为文本型
# msg = MIMEText('hello, send by ...', 'plain', 'utf-8')
##############################################

##############################################
#2、发送内容为html型
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
msg = MIMEText(mail_msg, 'html', 'utf-8')
##############################################


msg['From'] = _format_addr('你猜我是谁 <%s>' % from_addr)
msg['To'] = _format_addr('笨蛋 <%s>' % to_addr)
msg['Subject'] = Header('来自***的问候……', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

#已完成

