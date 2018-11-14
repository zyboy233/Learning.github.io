import json
import os

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

from utils.my_spider import my_main_api
from wechat.utils import do_reply,do_event,voice_trans

from wechatpy import parse_message
from wechatpy import WeChatClient
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import create_reply
from wechatpy.client.api import WeChatMaterial

# Create your views here.

TOKEN = 'zyboy'

@csrf_exempt
def handle_wx(request):
    # GET方式用于微信公众平台绑定验证
    if request.method == 'GET':
        signature = request.GET.get('signature','')
        timestamp = request.GET.get('timestamp','')
        nonce = request.GET.get('nonce','')
        echostr = request.GET.get('echostr','')
        try:
            check_signature(TOKEN,signature,timestamp,nonce)
        except InvalidSignatureException:
            echostr = 'error'
        response = HttpResponse(echostr,content_type="text/plain")
        return response
    else:
        msg = parse_message(request.body)
        print(msg)
        # 判断文本消息类型,文本消息处理
        if msg.type == 'text':
            reply = do_reply(msg)
        elif msg.type == 'voice':
            voice_trans()
            reply = create_reply('还没识别出来,稍等...',msg)
        elif msg.type == 'event':
            reply = do_event(msg)
        response = HttpResponse(reply.render(),content_type='application/html')
        return response
def create_menu(request):
    client = WeChatClient('wx892238d68ae6f860','dcb0a16bc13e183f3e20aa0fa30b23e6')
    client.menu.create({
        "button":[
            {
                "name": "app资讯",
                "sub_button": [
                    {
                        "type": "click",
                        "name": "最近应用更新",
                        "key": "kuan_update"
                    },
                    {
                        "type": "click",
                        "name": "应用推荐",
                        "key": "kuan_app_push"
                    },
                    {
                        "type": "click",
                        "name": "游戏推荐",
                        "key": "kuan_game_push"
                    }
                ]
            },
            {
                "name": "每日分享",
                "sub_button": [
                    {
                        "type": "click",
                        "name": "每日必应",
                        "key": "day_bing"
                    },
                    {
                        "type": "click",
                        "name": "每日歌曲",
                        "key": "day_music"
                    }
                ]
            },
            {
                "name":"人人影视",
                "sub_button":[
                    {
                        "type": "click",
                        "name": "影评",
                        "key": "m_review"
                    },
                    {
                        "type": "click",
                        "name": "片单推荐",
                        "key": "recom"
                    }
                ]
            }
        ]
    })
    return HttpResponse('ok')

@csrf_exempt
def add_image(request):
    # 上传临时素材并且存入数据库， 注意上传的图片名字不能是中文
    media_type = request.POST.get("media_type", "")
    media_file = request.FILES.get("media_file",'')
    title = request.POST.get("title", "")
    introduction = request.POST.get("introduction", "")
    client = WeChatClient('wx892238d68ae6f860', 'dcb0a16bc13e183f3e20aa0fa30b23e6')
    from wechatpy.client.api import WeChatMedia
    media = WeChatMedia(client)
    info = media.upload(media_type, media_file)
    print(info)
    return HttpResponse(info)