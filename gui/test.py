import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 设置发件人和收件人信息
sender_email = "UCAScourse@outlook.com"
receiver_email = "983578206@qq.com"
password = "38sUY:Q8?kLyXm5"  # 发件人邮箱密码

# 创建一个SMTP客户端
smtp_server = "smtp-mail.outlook.com"  # Outlook的SMTP服务器
port = 587  # Outlook SMTP端口号

# 创建一个MIMEMultipart对象来构建邮件
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "这是一个自动发送的邮件"

# 邮件正文
body = "这是一封自动发送的邮件，使用Python发送。"
message.attach(MIMEText(body, "plain"))

# 建立SMTP连接并登录
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    
    # 发送邮件
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("邮件发送成功")
except Exception as e:
    print("邮件发送失败:", str(e))
finally:
    # 关闭SMTP连接
    server.quit()
