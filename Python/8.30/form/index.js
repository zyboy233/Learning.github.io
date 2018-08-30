var express = require('express')
var bodyParser = require('body-parser')
var multer = require('multer')
var web = express()
var form = multer()
web.use(express.static('public'))
web.use(bodyParser.urlencoded({extended:false}))
// 如果使用的时FormDat这种数据提交方式的话
// 那么需要multer里面的array()方法进行数据剥离
web.post('/test',form.array(),function(req,res){
    name = req.body.name
    age = req.body.age
    fond = req.body.fond
    res.send('姓名是'+name + ",年龄是" + age + ',爱好是'+fond)
})

web.listen('8080',function(){
    console.log('服务器启动...')
})