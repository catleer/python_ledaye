"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def text_example():
    # print "发送文本邮件示例"

    # 邮件发送者
    sender = "sc_fw@boco.com.cn"

    # 邮件接收地址
    receivers = "chenle@boco.com.cn"

    msg = MIMEText("测试邮箱发送", "plain", "utf-8")
    msg["From"] = sender
    msg["To"] = receivers
    msg["Subject"] = Header("接口测试运行测试报告", "utf-8")

    # smtp服务
    smtpserver = "smtp.boco.com.cn"
    smtpport = 465
    username = "sc_fw@boco.com.cn"
    password = "boco#123"

    # 构建smtp对象
    smtp = smtplib.SMTP_SSL()

    # 连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    # print "连接结果： "
    # print con

    # 登录smtp服务
    log = smtp.login(username, password)
    # print "登录结果："
    # print log

    # 发送邮件
    # print receivers
    res = smtp.sendmail(sender, receivers, msg.as_string())
    # print "邮件发送结果： "
    # print res

    # 退出
    smtp.quit()
    # print "send email finish"

if __name__ == '__main__':
    text_example()