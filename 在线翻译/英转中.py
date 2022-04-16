# -*- encoding: utf-8 -*-
'''
@File    :   英转中.py
@Time    :   2022/04/15 22:57:21
@Author  :   NMOON 
@Version :   1.0
@Contact :   ay1054@qq.com
@Personal:   应无所往，而生其心
@Function:   英文转中文
@Desc    :   目前仅支持欧路词典翻译：1.只能翻译单词 2.单词句子都能翻译，但只有一个返回值
'''

# here put the import lib

import requests
import json
import lxml.html as lxml
from urllib import parse


class TranslateSpider(object):
    def __init__(self):
        self.urls = {
            '百度翻译': 'https://fanyi.baidu.com/pcnewcollection',  # f'https://fanyi.baidu.com/v2transapi?from={entozh[0]}&to={entozh[1]}'
            '欧路词典': 'https://dict.eudic.net/dicts/en/',  #'https://dict.eudic.net/dicts/prefix/',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39'
        }
        self.session = requests.Session()
        self.session.headers = headers

    def access_url(self, url):
        self.responce = self.session.get(url)
        return self.responce

    # def test(self, query):
    #     url = 'https://dict.eudic.net/dicts/prefix/'
    #     self.responce = self.session.get(url + query)
    #     return self.responce

    def getResults(self, query, ways='欧路词典'):

        self.responce = self.session.get(self.urls[ways] + parse.quote(query))
        # data = {
        #     'from': 'en',
        #     'to': 'zh',
        #     'query': query,
        #     'transtype': 'realtime',
        #     'simple_means_flag': 3,
        #     'sign': 56805.278228,
        #     'token': 'c9ce9c2cf83a739713dfdff69ca08c5b',
        #     'domain': 'common',
        # }
        # responce = self.session.post(self.urls[ways], data=data)
        return self.responce

    def write2html(self, name):
        with open(f'{name}.html', 'w', encoding='utf-8') as fw:
            fw.write(self.responce.text)

    def getlong(self, name):
        # 长句子返回
        url = 'https://dict.eudic.net/Home/TranslationAjax'
        data = {'to': 'en', 'text': name, 'contentType': 'text/plain'}
        self.responce = self.session.post(url, data)
        return self.responce

    def getInfoBylxml(self):
        html = lxml.fromstring(self.responce.text)
        result = html.xpath('//ol/li/text()')
        return "可选单词翻译：" + result

