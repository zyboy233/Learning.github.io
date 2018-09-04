var express = require('express')
var fs = require('fs')
var web = express()
web.use(express.static('public'))

var allMessage = []

fs.exists('data/info.json',function(isExists){
    if(!isExists){
        // directory 文件夹
        fs.mkdirSync('data')
    }
    else{
        // 获取之前所有的留言数据 并且将数据交给allMessage
        allMessage = JSON.parse('data/info.json')
    }
})

web.get('/messageSend',function(req ,res){
    // var content = req.query.content 
    // var time = req.query.time 
    // global
    req.query.content = req.query.content.replace(/</g,'&lt;')
    req.query.content = req.query.content.replace(/>/g,'&gt;')
    // unshift 将数据添加到列表当中的第一个位置
    allMessage.unshift(req.query)

    fs.writeFile('data/info.json',JSON.stringify(allMessage),function(err){
        if(err)
        {
            res.json({status:401,message:"留言失败"})
        }
        else{
            res.json({status:200,message:"留言成功"})
        }
    })
})
web.get('/allMessage',function(req, res){
    res.send(allMessage)
})
web.listen('8000',function(){
    console.log('服务器启动')
})
