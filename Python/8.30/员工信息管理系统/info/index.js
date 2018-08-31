var express = require('express')
var bodyParser = require('body-parser')
var multer = require('multer')
var fs = require('fs')
var web = express()
var form = multer()
web.use(express.static('public'))
web.use(bodyParser.urlencoded({extended:false}))


web.post('/addNew',form.array(),function(req,res){
    // 判断是否存在指定文件夹
    // 如果存在 则回调函数值为True
    // 如果不存在 则回调函数值为Flase
    fs.exists('data',function(isExists){
        if(!isExists){
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
            data:data,
            des:'新增员工'
        }
        var infoString = JSON.stringify(json)
        // 方法1:
        // fs.exists('data/info.txt',function(isExists){
        //     if(isExists){
        //         fs.readFile('data/info.txt',function(err,data){
        //             infoString = infoString + data
        //         })
        //     }
        // })
        // 方法2:
        // fs.writeFile('data/info.txt',infoString,{flag:'a'},function(err)
        // 方法3:
        fs.appendFile('data/info.txt',infoString + ',\n',function(err){
            if(err){
                console.log('写入失败')
                res.send(失败)
            }
            else{
                console.log('写入成功')
                res.send('成功')
            }
        })
    })
})

web.get('/getInfo',function(req,res){
    fs.exists('data',function(isExists){
        if(isExists){
            fs.readFile('data/info.txt',function(err,data){
                if(err){
                    res.send('读取失败')
                }
                else{
                    res.send(data)
                }
            })
        }
    })
})

web.listen('8080',function(req,res){
    console.log('服务器启动...')
})


// 1.index页面到new页面  window.location.href = 'new.html'
// 2.放置input标签 获取input标签 getElementByName()
//     后面不要追加.value  因为按照现在的代码
//     input输入框里没有来得及写入内容  程序就已经加载完毕
// 3.将数据发送给后台 xhr的form请求方式
//     var form = new FormData()
//     form.append()
// 4.后台接收到数据 '追加'到本地文件里面  appendFile
//     同时  注意拼接成json格式  所以在后面追加','
// 5.index页面进行数据请求 获取全部数据
// 6.后台接收到请求以后  读取本地文件 readFile
//     将读到的数据全部发送到前端  数据格式为
//     数据一,
//     数据二,
//     数据三,
//     数据的类型为字符串
// 7.前端接收数据  将数据格式改成标准json格式的字符串
//     然后转化成json JSON.parse()
//     再然后遍历  获取每一条数据进行拼接
//     显示到当前界面