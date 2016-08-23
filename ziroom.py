# coding: utf-8
from pyquery import PyQuery as pq
# import pymongo as pm
import urllib2 as u2
# import time

# mongo connetc
# client = pm.MongoClient('mongodb://127.0.0.1:27017/test')
# db = client.netdata
# collection = db.ziroom


def listUrl(ztype, zpage):
    return 'http://sh.ziroom.com/z/nl/z' + str(ztype) + '.html?p=' + str(zpage)


def detailUrl(zpage):
    return 'http://sh.ziroom.com/z/vr/' + str(zpage) + '.html'


def listPage(ztype, zpage):
    url = listUrl(ztype, zpage)
    try:
        page = u2.urlopen(url, timeout=12).read()
    except Exception:
        page = ''
    return page


def detailPage(zpage):
    url = detailPage(zpage)
    try:
        page = u2.urlopen(url, timeout=12).read()
    except Exception:
        page = ''
    return page

# type-1
for x in range(1, 27):
    page = ''
    while not page:
        page = listPage(1, x)
    dollar = pq(page)
    items = dollar('#houseList').children('li')
    for element in items:
        each_item = pq(element)
        print each_item.text()
        if each_item.hasClass('zry'):
            print 'pass'
            continue
        detail_href = each_item.find('.img:first').find('a').attr('href')
        print detail_href
        exit()
    exit()
