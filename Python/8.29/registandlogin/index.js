var express = require('express')
// post请求方式会将参数放入到请求体当中
// 所以需要引入解析请求体的模块
var bodyParser = require('body-parser')

var web = express()

web.use(express.static('public'))

// 设置对url进行编码 并且不允许url进行扩展
// 如果设置为false 那么参数只能为数值或者字符串
// 如果设置为True 那么参数为任意类型
web.use(bodyParser.urlencoded({extended:false}))

// 存储注册成功以后的账号和密码
account = ''
psw = ''

web.get('/regist',function(req,res){
    var password = req.query.psw

    var password2 = req.query.pswa

    var user = req.query.user

    if(user != account && password == password2){
        account = user
        psw = password
        res.send('恭喜注册登陆成功! 账号是' + user + ',密码是' + password + ',请妥善保管')
    }
    else{
        res.send('注册失败,账号已经注册或者密码不一致')
    }

    console.log(password)
    console.log(password2)
})

web.post('/login',function(req,res){
    var name = req.body.user
    var password = req.body.password

    if(name == account && password == psw){
        res.send('恭喜登陆成功')
    }
    else{
        res.send('登陆失败,请检查账号和密码')
    }
})

web.listen('8080',function(){
    console.log('服务器启动...')
})