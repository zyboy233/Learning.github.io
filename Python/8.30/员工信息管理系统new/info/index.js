var express = require('express')
var bodyParser = require('body-parser')
var multer = require('multer')
var fs = require('fs')
var web = express()
var form = multer()
web.use(express.static('public'))
web.use(bodyParser.urlencoded({ extended: false }))


web.post('/addNew', form.array(), function (req, res) {
    // 判断是否存在指定文件夹
    // 如果存在 则回调函数值为True
    // 如果不存在 则回调函数值为Flase
    fs.exists('data', function (isExists) {
        if (!isExists) {
            // 
            fs.mkdirSync('data')
        }
        //  var name = req.body.name;
        //  var job = req.body.job;
        //  var card = req.body.card
        //  var code = req.body.code
        //  var tel = req.body.tel
        //  var currentTime = req.body.currentTime
        //  var json = {
        //      name:name,
        //      job:job,
        //      card:card,
        //      code:code,
        //      tel:tel,
        //      currentTime:currentTime,
        //  }
        var data = req.body
        var json = {
            data: data,
            des: '新增员工'
        }
        var infoString = ''
        setTimeout(function () {
            fs.readFile('data/info.txt', function (err, data) {
                if (err) {
                    infoString = JSON.stringify(json)
                }
                else {
                    infoString = ',\n' + JSON.stringify(json)
                }
            })
        }, 100)
        setTimeout(function () {
            fs.appendFile('data/info.txt', infoString, function (err) {
                if (err) {
                    console.log('写入失败')
                    res.send(失败)
                }
                else {
                    console.log('写入成功')
                    res.send('成功')
                }
            })
        }, 300)

    })
})

web.get('/getInfo', function (req, res) {
    fs.exists('data', function (isExists) {
        if (isExists) {
            fs.readFile('data/info.txt', function (err, data) {
                if (err) {
                    res.send('读取失败,请先添加信用户')
                }
                else {
                    res.send(data)
                }
            })
        }
    })
})

web.listen('8080', function (req, res) {
    console.log('服务器启动...')
})