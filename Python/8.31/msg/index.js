var express = require('express')
var bodyParser = require('body-parser')
var multer = require('multer')
var fs = require('fs')
var web = express()
var form = multer()
web.use(express.static('public'))
web.use(bodyParser.urlencoded({extended:false}))

web.post('/newmsg',form.array(),function(req,res){
    fs.exists('data',function(isExists){
        if(!isExists){
            fs.mkdirSync('data')
        }
        var data = req.body
        var dataString = JSON.stringify(data)
        fs.appendFile('data/msg.txt',dataString + ',\n' ,function(err){
            if(err){
                console.log('写入失败')
                res.send('留言失败')
            }
            else{
                console.log('写入成功')
                res.send('留言成功')
            }
        })
    })
})
web.listen('8080',function(req,res){
    console.log('服务器启动...')
})