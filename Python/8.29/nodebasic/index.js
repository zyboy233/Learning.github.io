// 引入express模块  express模块为数据请求基础模块
// 如果发生数据请求 那么一定需要使用这个模块
var express = require('express')

// 创建模块的一个实例化对象
var web = express()

// static 静态 让web对象使用工程中的静态资源 public文件夹
web.use(express.static('public'))

// get 表示使用get方法 方法后面追加两个参数 
// 参数1: 请求的接口
// 参数2: 回调函数 
//     回调函数里面有两个参数
//     参数1: 前端从后端传的值
//     参数2: 后端往前端传的值
web.get('/book',function(req , res){
    res.send('<h1>古今奇书<<聊斋志异>></h1>')
    // res.json()
})

// 让程序监听node端口
web.listen('8080',function(){
    console.log('服务器启动......')
})