#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
from urllib.request import urlopen,Request


id = 2
url ='http://www.qiushibaike.com/textnew/page/'+str(id)



def get_qiubai(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    request = Request(url, headers=headers)
    response = urlopen(request)

    soup = BeautifulSoup(response, "html.parser")

    auther = soup.find_all('h2')
    title = soup.find_all('div', class_='content')

    max_len = len(auther)

    for num in range(max_len):
        print(auther[num].get_text().strip('\n') + '\n')
        print(title[num].get_text().strip('\n') + '\n\n')


if __name__ == '__main__':
    get_qiubai(url)
