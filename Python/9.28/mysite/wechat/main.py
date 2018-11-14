


from wechatpy import WeChatClient

client = WeChatClient("wx892238d68ae6f860", "dcb0a16bc13e183f3e20aa0fa30b23e6")
client.menu.create({
    "button":[
        {
            "type":"click",
            "name":"今日歌曲",
            "key":"V1001_TODAY_MUSIC"
        },
        {
            "type":"click",
            "name":"歌手简介",
            "key":"V1001_TODAY_SINGER"
        },
        {
            "name":"菜单",
            "sub_button":[
                {
                    "type":"view",
                    "name":"搜索",
                    "url":"http://www.soso.com/"
                },
                {
                    "type":"view",
                    "name":"视频",
                    "url":"http://v.qq.com/"
                },
                {
                    "type":"click",
                    "name":"赞一下我们",
                    "key":"V1001_GOOD"
                }
            ]
        }
    ]
})