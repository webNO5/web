#-*-coding:utf8-*-
import time
import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 
from email.mime.multipart import MIMEMultipart

def send_mail(subject, content,goal):
    MAIL_LIST = [goal] 
    MAIL_USER = "xidianweb4"
    MAIL_PASS = "yotlwvlctteseulw"
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


def signupmail(goal,check):
    title=u"欢迎注册SocialForuml"
    body=u'尊敬的用户：\n    您好！\n    欢迎注册SocialForum。您的验证码为：'+check+u' 。请在10分钟内完成注册！\n谢谢！\n[本邮件为系统自动发送，请勿回复]'
    title=title.encode('gb2312')
    body=body.encode('gb2312')
    return send_mail(title,body,goal)

def finishmail(goal,user):
    title=u"注册成功"
    body=u'亲爱的'+user+u'：\n    您好！\n    欢迎加入Socialfforum。\n    SocialForum全体工作人员祝您生活愉快！\n[本邮件为系统自动发送，请勿回复]'
    title=title.encode('gb2312')
    body=body.encode('gb2312')
    return send_mail(title,body,goal)


