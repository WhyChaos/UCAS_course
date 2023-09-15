import itchat

# 登录微信
itchat.auto_login(hotReload=True)

# 发送消息
receiver = 'Chaos'
message = '你好，这是通过Python发送的消息！'
itchat.send(message, toUserName=receiver)

# 退出登录
itchat.logout()
