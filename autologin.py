#!/usr/local/bin/python3
import urllib
from urllib import request
import http.cookies
schoolnumber = "yong"
password = "password"
url = "http://gw.bupt.edu.cn/"
ip = "http://10.3.8.212/"
#若无法连接，吧ip的值改为ip2的值
ip2 = "http://10.3.8.211/"
User_Agent = 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
def main():
    state = check_login_state()
    if state == '未登录':
        result = login(schoolnumber,password)
        print(result)
        info = if_login(result)
        return (info)
    elif state == '您已经成功登录。':
        return ('您已经成功登录。')
    else:
        return(state)
def check_login_state():
    try:
        req = request.Request(url)
        res = request.urlopen(req)
    except:
        req = request.Request(ip)
        res = request.urlopen(req)
    html = res.read().decode("gb2312")
    if len(html.split('上网注销窗')) == 2 or len(html.split('登录成功窗')) == 2:
        return('您已经成功登录。')
    elif len(html.split('欢迎登录北邮校园网络')) == 2:
        return('未登录')
    else:
        dict = {}
        dict['Status'] = res.status
        dict['reason'] = res.reason
        dict['getheaders'] = res.getheaders
        dict['html'] = html
        return('登陆失败'+str(dict))
def login(schoolnumber,password):
    try:
        req = request.Request(url)
        req.add_header('User-Agent',User_Agent)
        req.add_header("Cookie","myusername=%s"%(schoolnumber))
        req.add_header("Cookie","username=%s"%(schoolnumber))
        req.add_header("Cookie","smartdot=%s"%(password))
        postdata = urllib.parse.urlencode({'DDDDD': str(schoolnumber), 'upass': str(password), '0MKKey':'', 'savePWD':'0'})  
        postdata = postdata.encode('utf-8')  
        res = request.urlopen(req,postdata)
        return(res)
    except:
        req = request.Request(ip)
        req.add_header('User-Agent',User_Agent)
        req.add_header("Cookie","myusername=%s"%(schoolnumber))
        req.add_header("Cookie","username=%s"%(schoolnumber))
        req.add_header("Cookie","smartdot=%s"%(password))
        postdata = urllib.parse.urlencode({'DDDDD': str(schoolnumber), 'upass': str(password), '0MKKey':'', 'savePWD':'0'})  
        postdata = postdata.encode('utf-8')  
        res = request.urlopen(req,postdata)
        return(res)
def if_login(res):
    #if isinstance(res,http.client.HTTPResponse):
    html = res.read().decode("gb2312")
    if len(html.split('上网注销窗')) == 2 or len(html.split('登录成功窗')) == 2:
        return('您已经成功登录。')
    elif len(html.split('欢迎登录北邮校园网络')) == 2:
        return('登陆失败，请联系作者')
    else:
        dict = {}
        dict['Status'] = res.status
        dict['reason'] = res.reason
        dict['getheaders'] = res.getheaders
        return('登陆失败'+str(dict))
print(main())
