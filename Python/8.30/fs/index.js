// 引入文件读写模块 系统默认包含fs模块 所以无需下载
var fs = require('fs')

var gameRoleInfo = {
    name: '芽衣',
    level: '20',
    equipment: ['村正', '圣痕', '大砍刀', '高射炮', '萝莉装', '五速鞋'],
    blood: '3500',
    attack: '111',
    money: '3201'
}

// 将字典对象转化成字符串对象
var gameRoleInfoString = JSON.stringify(gameRoleInfo)

// writeFile后面跟三个值
// 1.写入文件的路径
// 2.写入的内容
// 3.写入以后的回调函数
fs.writeFile('data/game.txt',gameRoleInfoString,function(err){
    if(err){
        console.log('文件写入失败:',err)
    }
    else{
        console.log('文件写入成功')
    }
})
// readFile里面两个参数
// 参数1.读取的文件路径
// 参数2.读取文件以后的回调函数
// 回调函数里面有两个参数
// 参数1.读取失败以后的信息
// 参数2.读取成功以后的信息
fs.readFile('data/game.txt',function(err,data){
    if(err){
        console.log('读取失败',err)
    }
    else{
        // JSON.parse 将字典格式的字符串转化为字典对象
        // console.log('读取成功:'+JSON.parse(data))
        console.log('读取成功:')
        console.log(JSON.parse(data))
    }
})