"""
实现自动发送消息
"""
 
import time
import os
from pywinauto.keyboard import send_keys #键盘
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def open_app(app_dir):
    os.startfile(app_dir)

def send(message, username, wechat_path):
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 获取当前时间
    sent_time = time.strftime("%H:%M:%S", time.localtime())  # 发送时间
    if time_now == sent_time:  # 当前时间等于发送时间则执行以下程序

        app_dir = wechat_path  # 此处为微信的绝对路径
        open_app(app_dir)
        time.sleep(1)
 
        #进入微信，模拟按键Ctrl+F
        send_keys('^f')
        send_keys(username)
        time.sleep(1)
        send_keys('{ENTER}') # 回车键必须全部大小
 
        #需要发送的消息内容
        time.sleep(1)
 
        # 输入聊天内容
        send_keys(message)
        # 回车发送消息
        send_keys('{ENTER}')
 
        time.sleep(3)
        
def send_email(message_content, receiver_email):
    # 设置发件人和收件人信息
    sender_email = "UCAScourse@outlook.com"
    password = "密码"  # 发件人邮箱密码

    # 创建一个SMTP客户端
    smtp_server = "smtp-mail.outlook.com"  # Outlook的SMTP服务器
    port = 587  # Outlook SMTP端口号

    # 创建一个MIMEMultipart对象来构建邮件
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "UCAS课程容量提示"

    # 邮件正文
    body = message_content
    message.attach(MIMEText(body, "plain"))

    # 建立SMTP连接并登录
    flag = True
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        
        # 发送邮件
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("邮件发送成功")
    except Exception as e:
        flag = False
        print("邮件发送失败:", str(e))
    finally:
        # 关闭SMTP连接
        server.quit()
        return flag

        

 
 
 
 