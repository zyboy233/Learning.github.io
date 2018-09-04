var express = require('express')
var bodyParser = require('body-parser')
var multer = require('multer')
var web = express()
web.use(express.static('public'))
web.use(bodyParser.urlencoded({extended:false}))

var account = 545642
var fullName = ''
// disk 硬盘  storage 存储
// 当前配置信息不负责上传头像 上传头像由前端负责
// 当前配置信息只负责设置图片的存储路径和名称
var headerConfig = multer.diskStorage({
    // 存储的路径
    destination:'public/allHeaders' ,
    // 设置图片名称
    filename:function(req,file,callback){
        // 以'.'分割原始名称(验证码.png)
        var name  = file.originalname.split('.')

        var fileType = name[name.length - 1]

        account ++
        // callback回调函数生成图片的名称
        // 需要两个值:
        // 值1:错误信息
        // 值2:图片名称
        fullName = account + '.' + fileType
        callback(null,fullName)
    }
})
// 创建一个加载配置信息的upload对象
var upload = multer({storage:headerConfig})
// single 单个的

web.post('/upload',upload.single('photo'),function(req,res){
    res.send('')
})

web.get('/getHeader',function(req,res){
    res.send('allHeaders/' + fullName)
})

web.listen('8080',function(){
    console.log('服务器启动...')
})