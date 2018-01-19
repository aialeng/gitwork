# coding:utf-8

import requests,re
from lxml import etree

#定义请求地址url
url = "http://jandan.net/ooxx"

#定义请求头
headers = {
    "Host":"jandan.net",
    "Upgrade-Insecure-Requests":"1",
    "Cookie":"_ga=GA1.2.489157472.1515827032; _gid=GA1.2.1638883040.1515827032",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
}

#向指定url发送请求获取数据
response = requests.get(url,headers=headers)

content = response.text
# print(html_str)

#正则表达式筛选目标数据
pic_list = re.findall(r'"img":"(.*?)"',content)
print(pic_list)
