#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# auther: yueban

from urllib.parse import urlencode,quote
from urllib.request import urlopen,Request,HTTPCookieProcessor,build_opener
from bs4 import BeautifulSoup
import requests
from http.cookiejar import LWPCookieJar
import simplejson



session = requests.session()
session.cookies = LWPCookieJar(filename='BT_cookies')


# try:
#     session.cookies.load(ignore_discard=True)
# except:
#     print("Cookie 未能加载")



bt_url = 'http://www.cilibaba.com'


agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
headers = {
    'User-Agent': agent
}


def get_html(url):
    request = Request(url, headers=headers)
    response = urlopen(request)

    soup = BeautifulSoup(response, "html.parser")
    return soup

def str_to_bytes(date):
    data = bytes(date, encoding='utf8')
    return data

def get_url(KEY,PAGE):
    get_bt_data = {
        'c': '',
        's': 'create_time',
        'p': str(PAGE)
    }
    key = quote(KEY)
    get_bt_url_date = bt_url + '/search/'+ key +'/?'+ urlencode(get_bt_data)
    return get_bt_url_date


def get_curl(test_url):
    req = Request(test_url,headers=headers)
    opener = build_opener(HTTPCookieProcessor(session.cookies))
    response = opener.open(req)
    return response.read().decode()


def get_manage_link(href):
    data = {
        'hashes': href
    }
    url = bt_url+'/api/json_info'+'?'+urlencode(data)
    request = get_curl(url)
    # request = get_html(url)
    return request

def get_info_hash(href):
    t = ''.join(list(filter(str.isdigit, href)))
    test = get_manage_link(t)
    dictinfo = simplejson.loads(test)
    info_hash = dictinfo['result'][0]['info_hash']
    return info_hash


def get_title(KEY,PAGE):
    url = get_url(KEY,PAGE)
    session.get(url,headers=headers)
    session.cookies.save()
    soup = get_html(url)
    url = soup.find_all('td', class_='x-item')
    max_len = len(url)

    for x in range(max_len):
        title =  url[x].contents[1].contents[1].attrs['title']
        print(title)
        href = url[x].contents[1].contents[1].attrs['href']
        info_hash = get_info_hash(href)
        print('magnet:?xt=urn:btih:'+ info_hash + '\n')



if __name__ == '__main__':
    keywork = input('请输入电影名称\n>    ')
    # keywork = '地心引力'
    page = 1
    get_title(keywork, page)