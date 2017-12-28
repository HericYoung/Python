#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 《用Python写网络爬虫》学习代码
# 
# @Author: H3ric Young
# @Date:   2017-12-08 16:23:16
# @Last Modified by:   H3ric Young
# @Last Modified time: 2017-12-27 13:28:43

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                   $$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                                     $$$
# $                                                                                                        $$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$        $$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$$$$$
# $$$$$$$$$$$$$$$                      $$$$     $$$$$$$           $$$$$    $$$$     $$$$$$$$$$$$       $$$$$$$$$
# $$$$$$$$$$$$$                       $$$$      $$$$$$$            $$$    $$$     $$$$$$$$$$$$$       $$$$$$$$$$
# $$$$$$$$$$$$    $$$$$$$$$$$     $$$$$$        $$$$$$    $$$$     $$    $$$    $$$$$$$$$$$$$$      $$$$$$$$$$$$
# $$$$$$$$$$$     $$$$$$$$$$$    $$$$$$    $    $$$$$$    $$$$    $$$    $     $$$$$$$$$$$$$$      $$$$$$$$$$$$$
# $$$$$$$$$$$        $$$$$$$    $$$$$$    $$    $$$$$            $$$         $$$$$$$$$$$$$$$      $$$$$$$$$$$$$$
# $$$$$$$$$$$$        $$$$$$    $$$$$    $$$    $$$$           $$$$$         $$$$$$$$$$$$$$     $$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$      $$$$    $$$$$            $$$$    $$     $$$$    $     $$$$$$$$$$$$$     $$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$    $$$$     $$$$             $$$     $$$    $$$$    $$     $$$$$$$$$$$    $$$$$$$$$$$$$$$$$$$
# $$$$$$$$           $$$$$    $$$     $$$$$$    $$$    $$$$    $$$    $$$     $$$$$$$$$$    $$$$$$$$$$$$$$$$$$$$
# $$$$$$$          $$$$$$     $$     $$$$$$$    $$    $$$$$    $$     $$$$     $$$$$$$    $$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$  $$   $$$  $       $$   $$$  $$            $       $$  $      $$      $$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$   $     $  $$  $$$   $  $$$  $   $$$$$$   $$   $$  $$  $$  $$$$$  $$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$  $$        $  $$$$  $   $$$  $$    $$$$  $$$      $$   $      $$     $$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$   $  $$    $   $$$   $  $$$  $$$$$   $$  $$$   $   $$  $$  $$$$$$$$$  $$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$  $   $$   $$       $$$      $$      $$   $$$  $$   $   $             $$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import urllib #用于进行中文编码
import urllib.request as urllib2 #用于进行爬虫核心处理
import re
import itertools
from urllib.parse import urljoin

# -------------------网页下载-------------------------
# 初始版本
def download1_0(url):
	return urllib2.urlopen(url).read()

# 加入异常处理功能
def download2_0(url):
	print("Downloading:",url)
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print("Download error:",e.reason)
		html = None
	return html

# 加入对500错误进行的重连操作
def download3_0(url,num_retries=2):
	print("Downloading:",url)
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print("Download error:",e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download3_0(url,num_retries - 1)
		return html

# 自定义代理
def download4_0(url,user_agent='Heric',num_retries=2):
	print("Downloading:",url)
	headers = {'User-agent':user_agent}
	request = urllib2.Request(url,headers=headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print("Download error:",e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download4_0(url,user_agent,num_retries-1)
	return html

# -------------------网页下载end-------------------------


# -------------------多连接爬取控制---------------------
# 根据网页地图获取网站链接
def crawl_sitemap(url):
	sitemap = download4_0(url)
	sitemap = sitemap.decode(encoding='utf-8')
    # sitemap = sitemap.encode("UTF-8"）

	links = re.findall('<loc>(.*?)</loc>',sitemap)
	for link in links:
		html = download4_0(link)

# 获取html代码中的a标签的href链接
def get_links(html):
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	return webpage_regex.findall(html)

# 链接爬虫
def link_crawler(seed_url,link_regex):
	crawl_queue = [seed_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = download4_0(url)
		html = html.decode(encoding='utf-8')
		save_resource("./test.html",html)
		for link in get_links(html):
			if re.match(link_regex,link):
				link = urljoin(seed_url,link)
				crawl_queue.append(link)

# 增加记录已爬取链接的功能
def link_crawler2_0(seed_url,link_regex):
	crawl_queue = [seed_url]

	seen = set(crawl_queue)

	while crawl_queue:
		url = crawl_queue.pop()
		html = download4_0(url)
		html = html.decode(encoding='utf-8')
		for link in get_links(html):
			if re.match(link_regex,link):
				link = urljoin(seed_url,link)
				if link not in seen:
					seen.add(link)
					crawl_queue.append(link)

# -------------------多连接爬取控制end---------------------


# -------------------保存网页代码到文件---------------------

# 将爬取到的页面代码保存到文件中
def save_resource(file,code):
	with open(file, 'w') as f:
		f.write(code)

# -------------------保存网页代码到文件end---------------------



# --------------------测试操作-----------------------
if __name__ == '__main__':

# --------------------------------------------------------------
	'''
	url = "http://example.webscraping.com/sitemap.xml"
	print(download4_0(url))
	crawl_sitemap(url)
	'''
# --------------------------------------------------------------
	'''
	for page in itertools.count(1):
		url = "http://example.webscraping.com/view/-%d" % page
		html = download4_0(url)
		if html is None:
			break
		else:
			pass
	'''
# ----------------------------------------------------------
	'''
	max_errors = 5
	num_errors = 0
	for page in itertools.count(1):
		url = "http://example.webscraping.com/view/-%d" % page
		html = download4_0(url)
		if html is None:
			num_errors += 1
			if num_errors == max_errors:
				break
		else:
			num_errors = 0
			save_resource("./test.html",html.decode(encoding='utf-8'))
	'''

# ---------------------------------------------------------
	link_crawler2_0("http://example.webscraping.com",'/places/')


# -------------------测试操作end---------------------
