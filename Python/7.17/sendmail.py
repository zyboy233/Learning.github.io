
from smtplib import SMTP_SSL,SMTP
from email.mime.text import MIMEText
from email.header import Header
import requests,json

def getWeatherInfo():
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E%E5%B8%82&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
    response = requests.get(url)
    dataJson = json.loads(response.text)
    msg = "\n"

    for data in dataJson["results"]:
        for index in data["index"]:
            msg = msg+index["des"]+'\n'
        wd = data["weather_data"][0]
        date = wd["date"]
        msg1 = "地点：郑州，日期：" + date
        msg =msg1+ "\n温度：" + wd["temperature"] +"，天气：" + wd["weather"] + "，风力：" + wd["wind"] + "\n温馨提示："+msg
        return msg
# getWeatherInfo()
def send():
    sender = '1797190195@qq.com'
    receivers = ['451253127@qq.com','496672009@qq.com','1450543861@qq.com','1342585981@qq.com','1421534615@qq.com']
    host_server = 'smtp.qq.com'
    pwd = "jktarqhsggqyhfhd"
    mail_content = getWeatherInfo()
    mail_title = "天气预报"
    smtp = SMTP_SSL(host_server,465)
    # 调试
    # smtp.set_debuglevel(1)
    # smtp.ehlo(host_server)
    smtp.login(sender,pwd)
    msg = MIMEText(mail_content,"plain","utf-8")
    msg["Subject"] = Header(mail_title,'utf-8')
    msg["From"] = sender
    for i in receivers:
        msg["To"] = i
    smtp.sendmail(sender,receivers,msg.as_string())
    print("Success")
    smtp.quit()

if __name__ == "__main__":
    send()