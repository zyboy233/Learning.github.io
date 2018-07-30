import  re
from urllib.request import Request,urlopen

base_url = 'https://www.qiushibaike.com/hot/page/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
ip_list = [
    '223.241.116.66:18118',
    '125.120.200.49:6666',
    '221.228.17.172:8181',
    '122.72.18.34:80',
    '218.241.234.48:8080',
    '120.26.110.59:8080'
]

def down_load_qiubai_info(pageIndex):
    full_url = base_url + str(pageIndex) +'/'
    request = Request(full_url,headers = headers)
    response = urlopen(request)
    # 获取对应网页的全部内容
    # decode()解码
    code = response.read().decode()

    # 正则匹配的内容  从制定的开始位置  到全部内容结束
    # 所以只需要指定开始的位置  不需要指定结束的位置
    #
    # 如果我们想要正则获取某一对标签里面的内容的时候
    # 那么需要将这对标签对写完整 而且在想要获取的内容
    # 上添加() 例如: <h2>(.*?)</h2>
    # pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender .*?Icon">(.*?)</div>.*?<a href="(.*?)"',re.S)
    # result = pattern.findall(code)
    # # print(result)
    # for name,age,article_url in result:
    #     # 去掉开始和结尾的换行符
    #     name = name.strip('\n')
    #     article_url = article_url.strip('\n').replace('<br/>','')
    #     print('作者是:',name)
    #     print('年龄是:',age)
    #     print('内容是:',article_url)

    pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>.*?<a.*?href="(.*?)".*?>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
    result = pattern.findall(code)
    for name,age,href,content,number,comments in result:
        name = name.strip('\n')
        age = age.strip('\n')
        href = href.strip('\n')
        content = content.strip('\n')
        number = number.strip('\n')
        comments = comments.strip('\n')
        print('作者是:',name)
        print('年龄是:',age)
        print('详情是:',href)
        print('内容是:',content)
        print('好笑数:',number)
        print('评论数:',comments)
        if int(comments) !=0:
            get_all_comment_with(href)
        else:
            print('该内容暂无评论')

def get_all_comment_with(url):
    detail_url = 'https://www.qiushibaike.com' + url
    print(detail_url)
    request = Request(detail_url,headers=headers)

    response = urlopen(request)
    code = response.read().decode()
    # print(code)
    pattern = re.compile(r'<div class="replay".*?<a href="(.*?)" class="userlogin".*?title="(.*?)">.*?<span class="body">(.*?)</span>',re.S)
    result = pattern.findall(code)
    print(result)
    print('---------------------------------------------------------------')
for i in range(1,14):
    down_load_qiubai_info(i)