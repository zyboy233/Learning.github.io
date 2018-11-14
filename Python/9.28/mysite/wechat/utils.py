import json
import  base64

from urllib.request import urlretrieve
from utils.my_spider import my_main_api,get_weather
from utils.aiapi import AiPlat

from wechatpy import create_reply,WeChatClient
from wechatpy.client.api import WeChatMedia
from wechatpy.replies import MusicReply

def do_reply(msg):
    if '天气:' in msg.content:
        # msg.content 就是发送过来的消息内容
        reply = get_weather(msg.content.split(':')[1],msg)
    elif '翻译:' in msg.content:
        tran_rsp = trans(msg.content.split(':')[1])
        reply = create_reply('译文: ' + tran_rsp,msg)
    else:
        reply = create_reply('抱歉,我们没有这个关键词!',msg)
    return reply

# 响应用户关注和取消相关的事件
def do_event(msg):
    if msg.event == 'subscribe':
        reply = create_reply('欢迎关注公众号,请按如下格式查询内容:\n"天气:北京"\n"翻译:文本"',msg)
    elif msg.event == 'unsubscribe':
        pass
    elif msg.event == 'click':
        reply = my_main_api(msg)
    else:
        reply = create_reply('我们不知道这个事件类型是什么',msg)
    return reply

def trans(str_text):
    """文本翻译"""
    app_key = 'vEQWKdz21sJaplLT'
    app_id = '2109279359'
    type_id = 0
    ai_obj = AiPlat(app_id, app_key)
    # 请求
    rsp = ai_obj.getNlpTextTrans(str_text, type_id)
    if rsp['ret'] == 0:
        respDic = dict(rsp, ensure_ascii=False, sort_keys=False, indent=4)
        trans_text = respDic['data']['trans_text']
        return trans_text
    else:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
        return '文本翻译失败'

def voice_trans():
    """语音识别"""
    client = WeChatClient('wx892238d68ae6f860','dcb0a16bc13e183f3e20aa0fa30b23e6')
    media = WeChatMedia(client)
    # voice_url = media.get_url('RW2WQZ86jVg9e0nkRyCzetdCedkIeE1W2QC37hUb3UEh_B-ttADCIhtQFZ0nthoR')
    # urlretrieve(voice_url,'test.amr')
    voice_response = media.download('RW2WQZ86jVg9e0nkRyCzetdCedkIeE1W2QC37hUb3UEh_B-ttADCIhtQFZ0nthoR')
    with open('../utils/test.amr','wb') as f:
        f.write(voice_response)
    return ''