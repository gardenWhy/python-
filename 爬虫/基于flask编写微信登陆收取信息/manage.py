#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from flask import Flask, request, render_template, session, jsonify
import time
import requests
import re
from bs4 import BeautifulSoup
import json

app = Flask(__name__)
app.debug = True
app.secret_key = 'asdasd'


def xml_parser(text):
    dic = {}
    soup = BeautifulSoup(text, 'html.parser')
    div = soup.find('error')
    for item in div.find_all(recursive=False):  # recursive设置为False就不会往下递归找子子孙孙
        dic[item.name] = item.text
    return dic


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        ctime = str(int(time.time() * 1000))
        qcode_url = 'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={}'. \
            format(ctime)
        ret = requests.get(qcode_url)
        qcode = re.findall('uuid = "(.*)";', ret.text)[0]
        session['qcode'] = qcode
        # print(qcode)

        return render_template('login.html', qcode=qcode)
    else:
        pass


@app.route('/check_login')
def check_login():
    response = {'code': 408}
    qcode = session.get('qcode')
    ctime = str(int(time.time() * 1000))
    check_url = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={}&tip=0&r=-1773517724&_={}".format(
        qcode, ctime)
    # 长轮训，检测是否扫码成功
    ret = requests.get(check_url)
    # print(ret.text)
    if "code=201" in ret.text:
        # 扫码成功
        src = re.findall("userAvatar = '(.*)';", ret.text)[0]
        response['code'] = 201
        response['src'] = src
    elif 'code=200' in ret.text:
        # 确认登陆
        redirect_uri = re.findall('redirect_uri="(.*)";', ret.text)[0]

        # 向redirect_uri发送请求,获取相关凭证信息
        redirect_uri = redirect_uri + '&fun=new&version=v2&lang=zh_CN'
        ticket_ret = requests.get(redirect_uri)
        ticket_dict = xml_parser(ticket_ret.text)
        # print(ticket_dict)
        session['ticket_dict'] = ticket_dict
        session['ticket_cookie'] = ticket_ret.cookies.get_dict()
        # print(session)
        response['code'] = 200
    return jsonify(response)


@app.route('/index')
def index():
    ticket_dict = session.get('ticket_dict')
    init_url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-1777548922&lang=zh_CN&pass_ticket={}'.format(
        ticket_dict.get('pass_ticket'))
    data_dict = {
        "BaseRequest": {
            "DeviceID": "e844751855056106",
            "Sid": ticket_dict.get('wxsid'),
            "Skey": ticket_dict.get('skey'),
            "Uin": ticket_dict.get('wxuin')
        }
    }
    init_ret = requests.post(
        init_url,
        json=data_dict
    )
    init_ret.encoding = 'UTF-8'
    # print(init_ret.json())
    # for item in init_ret.json()['ContactList']:
    #     print(item['NickName'])
    user_dict = init_ret.json()
    # print(user_dict['SyncKey'])
    session['SyncKey'] = user_dict['SyncKey']
    session['current_user'] = user_dict['User']
    return render_template('index.html', user_dict=user_dict)


@app.route('/get_img')
def get_img():
    """
    获取头像
    :return:
    """
    current_user = session['current_user']
    ticket_cookie = session.get('ticket_cookie')
    img_url = 'https://wx2.qq.com' + current_user['HeadImgUrl']

    img_ret = requests.get(img_url, cookies=ticket_cookie, headers={'Content-Type': 'image/jpeg',
                                                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'})
    # print(img_ret.text)
    return img_ret.content


# https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket=VlLwdrZup%252Bkyx9rCtLpIg6YM3MRYMZx0CV2uijdWo0koDD2h4AQRPnKDcgs%252Fxv0u&r=1531039751230&seq=0&skey=@crypt_4d5a4e5f_14f5f2c8636f61ec9997e06c6f55b3f3
@app.route('/user_list')
def user_list():
    """
    获取所有联系人
    :return:
    """
    ctime = str(int(time.time() * 1000))
    ticket_dict = session['ticket_dict']
    pass_ticket = ticket_dict.get('pass_ticket')
    skey = ticket_dict.get('skey')
    ticket_cookie = session.get('ticket_cookie')
    user_list_url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket={0}&r={1}&seq=0&skey={2}'.format(
        pass_ticket, ctime, skey)
    user_list_ret = requests.get(user_list_url, cookies=ticket_cookie)
    user_list_ret.encoding = 'utf-8'
    wx_user_dict = user_list_ret.json()
    # for item in wx_user_list:
    #     print(item)
    # print(ticket_cookie)
    # print(wx_user_dict['MemberCount'])
    # for item in wx_user_dict['MemberList']:
    #     print(item)

    return render_template('user_list.html', wx_user_dict=wx_user_dict)


@app.route('/send', methods=['GET', 'POST'])
def send():
    ctime = str(int(time.time() * 1000))
    if request.method == 'GET':
        return render_template('send.html')

    current_user = session['current_user']
    ticket_dict = session.get('ticket_dict')
    from_user = current_user['UserName']
    to = request.form.get('to')
    content = request.form.get('content')
    print(content)

    msg_url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}'.format(
        ticket_dict['pass_ticket'])
    data_dict = {
        'BaseRequest': {
            'DeviceID': "e849329259832869",
            "Sid": ticket_dict.get('wxsid'),
            "Skey": ticket_dict.get('skey'),
            "Uin": ticket_dict.get('wxuin')
        },
        'Msg': {
            'ClientMsgId': ctime,
            'Content': content,
            'FromUserName': from_user,
            'LocalID': ctime,
            'ToUserName': to,
            'Type': 1
        },
        'Scene': 0
    }
    ret = requests.post(msg_url, data=json.dumps(data_dict, ensure_ascii=False).encode('utf-8'))
    return render_template('send.html', ret=ret.text)

'''
请求/get_msg
在后台获取消息，
'''
@app.route('/get_msg')
def get_msg():
    return render_template('get_msg.html')


@app.route('/check_msg')
def check_msg():
    ticket_dict = session.get('ticket_dict')
    ctime = str(int(time.time() * 1000))
    SyncKey = session.get('SyncKey')
    ticket_cookie = session.get('ticket_cookie')
    sync_data_list = []
    for item in SyncKey['List']:
        temp = "%s_%s" % (item['Key'], item['Val'])
        sync_data_list.append(temp)
    sync_data_str = "|".join(sync_data_list)
    check_msg_url = 'https://webpush.wx2.qq.com/cgi-bin/mmwebwx-bin/synccheck'
    sync_dict = {
        'r': ctime,
        'skey': ticket_dict.get('skey'),
        'sid': ticket_dict.get('wxsid'),
        'uin': ticket_dict.get('wxuin'),
        'deviceid': 'e058806361330616',
        'synckey': sync_data_str,
        '_': '1531204044573',
    }
    check_ret = requests.get(check_msg_url, params=sync_dict, cookies=ticket_cookie)
    # 做到这，检查有没有消息
    # print(sync_data_str)
    # print(SyncKey)
    # print(ticket_cookie)
    # print(check_ret.text)

    if 'selector:"2"' in check_ret.text:
        msg_url = "https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsync"
        msg_params_dit = {
            'sid': ticket_dict.get('wxsid'),
            'skey': ticket_dict.get('skey'),
            'lang': 'zh_CN',
            'pass_ticket': ticket_dict.get('pass_ticket')
        }
        msg_dict = {
            'BaseRequest': {
                'DeviceID': 'e704036170768828',
                'Sid': ticket_dict.get('wxsid'),
                'Skey': ticket_dict.get('skey'),
                'Uin': ticket_dict.get('wxuin')
            },
            'SyncKey': SyncKey,
            'rr': '2087689925'
        }
        # print(SyncKey)
        ret = requests.post(msg_url, params=msg_params_dit, json=msg_dict, cookies=ticket_cookie)
        ret.encoding = 'utf-8'
        ret_msg_json = json.loads(ret.text)
        session['SyncKey'] = ret_msg_json['SyncKey']
        ret = ''
        for item in ret_msg_json['AddMsgList']:
            print(item['Content'], '=====', item['FromUserName'], '---->', item['ToUserName'])
        # print(ret.json())
    return check_ret.text


if __name__ == '__main__':
    app.run()
