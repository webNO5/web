#-*-coding:utf8-*-
import time
import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 
from email.mime.multipart import MIMEMultipart

def send_mail(subject, content,goal):
    MAIL_LIST = [goal] 
    MAIL_USER = "xidianweb4"
    MAIL_PASS = "131213"
    MAIL_POSTFIX = "163.com"
    MAIL_FROM = MAIL_USER + "<"+MAIL_USER + "@" + MAIL_POSTFIX + ">"
    try:
        message = MIMEMultipart() 
        message.attach(MIMEText(content)) 
        message["Subject"] = subject 
        message["From"] = MAIL_FROM 
        message["To"] = ";".join(MAIL_LIST) 
        smtp = smtplib.SMTP('smtp.163.com:25') 
        #smtp.connect('mail.163.com:25')
        smtp.login(MAIL_USER, MAIL_PASS) 
        smtp.sendmail(MAIL_FROM, MAIL_LIST, message.as_string()) 
        smtp.quit()
        rt='succeed'
        return rt
    except Exception,errmsg: 
        rt= "Send mail failed to"+str(errmsg) 
        return rt


result=send_mail("测试",'测试邮件','544549895@qq.com')
print result
