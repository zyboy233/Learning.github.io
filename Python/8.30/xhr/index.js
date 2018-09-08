var express = require('express')
var bodyParser = require('body-parser')
var web = express()
web.use(express.static('public'))
web.use(bodyParser.urlencoded({extended:false}))

web.get('/getTest',function(req,res){
    var name = req.query.name

    var des = req.query.des

    setTimeout(function(){
        res.send('听说有一种' + des + "非常厉害,叫做" + name)
    },2000)
})
web.post('/postTest',function(req,res){
    var star = req.body.star
    var des = req.body.des

    setTimeout(function(){
        res.send('商品评价成功')
    },2000)
})
web.listen('8080',function(){
    console.log('服务器启动成功...')
})

// xhr数据请求流程:
// 1.初始化xhr对象
//     设置请求方法  以及请求接口 open() xhr.readyState = 0
//     开始发送数据 send() xhr.readyState
// 2.后端接收前端发送过来的数据
//     req.query.XX get
//     req.body.XX post
// 3.将数据从后台返回给前端
//     xhr.readyState = 2
//     res.send() 发送数据到前端
// 4.前端接收后台发送过来的数据
//     接收部分数据时 xhr.readyState = 3
//     全部接收完毕 xhr.readyState =4