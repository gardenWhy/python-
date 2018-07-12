#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup

text = """
<error>
    <ret>0</ret>
    <message></message>
    <skey>@crypt_4d5a4e5f_ae6132d2fb600ed4e3d8b934c61a4482</skey>
    <wxsid>Dt8SrObNe9NxQN00</wxsid>
    <wxuin>868688925</wxuin>
    <pass_ticket>sPlzcsUJyE%2FSCHZP3VvBvbqzolLgSqtKSONIEPsanPvHbtuseIKUfiWWB7LzGTMu</pass_ticket>
    <isgrayscale>1</isgrayscale>
</error>
"""
def xml_parser(text):
    dic = {}
    soup = BeautifulSoup(text,'html.parser')
    div = soup.find('error')
    for item in div.find_all(recursive=False): # recursive设置为False就不会往下递归找子子孙孙
        dic[item.name] = item.text
    return dic
dic = xml_parser(text)