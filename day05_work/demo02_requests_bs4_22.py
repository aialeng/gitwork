# coding:utf-8

import requests,re
from bs4 import BeautifulSoup

#定义请求地址url
url = "http://jandan.net/drawings"

#定义请求头
headers = {
    "Host":"jandan.net",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
}

#向指定url发送请求获取数据
response = requests.get(url,headers=headers)

#获取网页数据
soup = BeautifulSoup(response.text)
print(soup)


img_src = soup.select(".text p img[src]")
print(img_src)

# img_src = soup.find_all("img")
# print(img_src)


for img_s in img_src:
    pic_url = img_s.attrs['src']
    print(">>>>>>>>>>>>开始保存图片%s" % pic_url)

    response2 = requests.get(pic_url, headers=headers)
    print(response2.content)  #<!-- a padding to disable MSIE and Chrome friendly error page -->

    response2.content = response2.content.replace("<title>","")
    print(response2.content)
    #储存图片
    # filename = pic_url[-30:]
    # with open("jd_img/" + filename,"wb") as f:
    #     f.write(response2.content)
    # print("<<<<<<<<<<<<保存完成")
