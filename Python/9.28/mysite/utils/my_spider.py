import requests
import json
import random
import sqlite3

from lxml import etree

from wechatpy import create_reply
from wechatpy.replies import ImageReply,MusicReply,ArticlesReply
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMaterial


# 调用
def my_main_api(msg):
    kuan = Kuan()
    if msg.key == 'kuan_update':
        reply = kuan.get_update(msg)
    elif msg.key == 'kuan_app_push':
        reply = kuan.get_app_push(msg)
    elif msg.key == 'kuan_game_push':
        reply = kuan.get_game_push(msg)
    elif msg.key == 'day_bing':
        bing = DayBing()
        reply = bing.get_image_url(msg)
    elif msg.key == 'day_music':
        # http://music.163.com/song/522510615/?userid=311948152
        reply = MusicReply(message=msg,title='千禧',thumb_media_id='EpZ4EJF9njZOorkr2TnVAquSxXF2eoQW2Bk6DdKS07kycz-hwYnRSLAmfubPNvzh',
                           description='徐秉龙',music_url='http://www.ytmp3.cn/down/54100.mp3',
                           hq_music_url='http://www.ytmp3.cn/down/54100.mp3')
    elif msg.key == 'm_review':
        ren = RenRen()
        news = ren.get_info()
        reply = ArticlesReply(message=msg)
        print(news)
        for new in news:
            reply.add_article({
                'title': new['title'],
                'description': new['description'],
                'image': new['image'],
                'url': new['url']
            })
    elif msg.key == 'recom':
        ren = RenRen()
        ren.url = 'http://www.zimuzu.tv/article?type=recom'
        news = ren.get_info()
        reply = ArticlesReply(message=msg)
        # print(news)
        articles = [
            {
                'thumb_media_id': 'Pp8iDnCrxFlb8CUfmmpGOYuoj3EisK_t4xtHvBA_blg',
                'title': '哈哈哈哈',
                'content': '红红火火恍恍惚惚红火火恍恍惚惚',
                'author': '张宇',
                'content_source_url': 'http://mp.weixin.qq.com/s?__biz=MzUxNzk3MTQ5NA==&mid=100000003&idx=1&sn=85ac89b7f597ebae2ea6373d3a2e922b&chksm=79914a4a4ee6c35c3c9c4147ea169692df3a84feeb992d442848f2c67ccd5de1e90e905d7af7#rd',
                'digest': '你好',
                'show_cover_pic': '1',
            }
        ]
        # 上传永久素材
        # client = WeChatClient('wx892238d68ae6f860', 'dcb0a16bc13e183f3e20aa0fa30b23e6')
        # material = WeChatMaterial(client)
        # 图片
        # obj_file = open('test.jpg','rb')
        # resp = material.add('thumb',obj_file,'缩略图.test')
        # 图文
        # resp = material.add_articles(articles)
        # 获取素材
        # resp = material.get('Pp8iDnCrxFlb8CUfmmpGOaF0tYuqXkQKNn0qufc5HsA')
        # print(resp)
        for new in news:
            reply.add_article({
                'title': new['title'],
                'description': new['description'],
                'image': new['image'],
                'url': 'http://mp.weixin.qq.com/s?__biz=MzUxNzk3MTQ5NA==&mid=100000003&idx=1&sn=85ac89b7f597ebae2ea6373d3a2e922b&chksm=79914a4a4ee6c35c3c9c4147ea169692df3a84feeb992d442848f2c67ccd5de1e90e905d7af7#rd'
            })
    else:
        reply = ''
    return reply

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
class Kuan(object):
    """酷安主页爬虫"""
    def __init__(self):
        self.url = 'https://www.coolapk.com/'
    # 获取主页源码
    def get_code_with_url(self,url):
        response = requests.get(url,headers=headers)
        root = etree.HTML(response.content)
        sections = root.xpath('//div[@class="ApplicationToRecommend"]')
        return sections
    # 获取最近更新
    def get_update(self,msg):
        sections = self.get_code_with_url(self.url)
        names = sections[0].xpath('.//span[@class="sp-name"]/text()')
        updates = sections[0].xpath('.//span[@class="sp-time"]/text()')
        context = ""
        for name,update in zip(names,updates):
            context += name + ': ' + update + '\n'
        reply = create_reply(str(context)[:-2], msg)
        return reply
    # 获取应用推荐
    def get_app_push(self,msg):
        sections = self.get_code_with_url(self.url)
        names = sections[1].xpath('.//span[@class="sp-name"]/text()')
        downloads = sections[1].xpath('.//span[@class="sp-time"]/text()')
        context = ""
        for name, update in zip(names, downloads):
            context += name + ': ' + update + '\n'
        reply = create_reply(str(context)[:-2], msg)
        return reply
    # 获取游戏推荐
    def get_game_push(self,msg):
        sections = self.get_code_with_url(self.url)
        names = sections[2].xpath('.//span[@class="sp-name"]/text()')
        deses = sections[2].xpath('.//span[@class="sp-time"]/text()')
        context = ""
        for name, update in zip(names, deses):
            context += name + ': ' + update + '\n'
        reply = create_reply(str(context)[:-2], msg)
        return reply

class DayBing(object):
    """每日必应json:http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"""
    def get_image_url(self,msg):
        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
        response = requests.get(url,headers=headers)
        strJson = json.loads(response.content)
        url = 'http://s.cn.bing.net' + strJson['images'][0]['url']
        context = ''
        context += '<a href="{}">每日必应图片</a>'.format(url)
        # reply = create_reply(str(context), msg)
        reply = ImageReply(message=msg,media_id='Ve1pve6vOfZerye0t8gV8V6DKiEC-hOvsZRMdHmK5-oRZuHZspMlJSsn9ei2_N0o')
        return reply

def get_weather(city,msg):
    """获取天气信息"""
    url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=&qq-pf-to=pcqq.group'.format(city)
    response = requests.get(url,headers=headers)
    strJson = json.loads(response.text)
    weather_data = ''
    for day in strJson['results'][0]['weather_data']:
        weather_data += day['date'] + '\n' + day['weather'] + '\n' + day['wind'] + '\n' + day['temperature'] + '\n'
    reply = create_reply(weather_data,msg)
    return reply

class RenRen(object):
    """人人影视网站"""
    def __init__(self):
        self.url = 'http://www.zimuzu.tv/article?type=m_review'
    def get_code_with_url(self):
        response = requests.get(self.url, headers=headers)
        root = etree.HTML(response.content)
        li_list = root.xpath('//div[@class="article-list"]/ul/li')[:15]
        return li_list
    def get_info(self):
        li_list = self.get_code_with_url()
        news = [random.choice(li_list) for _ in range(3)]
        info = []
        for index,li in enumerate(news):
            title = li.xpath('.//h3/a/text()')[0]
            url = 'http://www.zimuzu.tv' + li.xpath('.//h3/a/@href')[0]
            description = li.xpath('.//div[@class="fl-info"]/p/text()')[0]
            image = li.xpath('.//div[@class="fl-img"]/a/span/img/@src')[0]
            info.append({'title':title,'url':url,'description':description,'image':image})
            # self.get_article_with_url(url)
        return info
    def get_article_with_url(self,url):
        # 获取文章内容, 待填
        response = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            'Referer':'http://www.zimuzu.tv/article'
        })
        print(response.text)