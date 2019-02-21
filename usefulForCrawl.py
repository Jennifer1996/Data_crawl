#!/usr/bin/env python
#coding=utf8
import urllib.request
import time

def get_html_content_from_a_page(url,time_sleep = 0):
    try:
        time.sleep(time_sleep)
        req = urllib.request.Request(url)
        browser='Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'
        req.add_header('User-Agent',browser)
        response = urllib.request.urlopen(req) 
        html_content=response.read()
        return html_content
    except:
        return ''

def download_page(filename,url,mode_type = 'wb+',time_sleep = 0):
    content = get_html_content_from_a_page(url,time_sleep = time_sleep)
    open(filename,mode_type).write(content)

if __name__ == '__main__':
    url = 'https://www.chunyuyisheng.com/pc/qa/48MYNJutH5ykZBEt_aTxkg/'
    download_page('/Users/chensi/Desktop/Tencent-Project/a.html',url)





