# -*- coding: utf-8 -*-
# urllib.request模块基本使用
# 
# @Author: H3ric Young
# @Date:   2017-12-08 11:15:23
# @Last Modified by:   H3ric Young
# @Last Modified time: 2017-12-09 01:02:25


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

import urllib.request as urllib #用于网页数据抓取的操作模块

url = "https://www.baidu.com"

# 浏览器信息
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"

#伪装浏览器访问
my_header={'User-Agent':user_agent}

# 创建request对象
request = urllib.Request(url,headers=my_header)

# request.add_header("User-agent", user_agent)

#第一个字母大写，后面的全部小写，
#新增/修改时参数"User-agent"、"User-Agent"均可
#读取时只能使用"User-agent"
#无语，暂时未知原因
agent = request.get_header("User-agent")

# print(agent)

#  urlopen(url, data, timeout) 或者直接传一个Request对象作为参数
#  参数：
#  1.链接
#  2.传送数据
#  超时时间
response = urllib.urlopen(request)

# read() 返回获取到的网页内容
content = response.read()

print(content)