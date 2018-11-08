from flask import Flask
from flask import request
import json
import requests


app = Flask(__name__)

def senddata(corpsecret,user,sectionid,agentid,subject,content):

    corpid = 'ww73460d4b034fb644'   #CorpID是企业号的标识

    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    try:
        token_file = requests.get(gettoken_url)
    except Exception as e:
        print(e)
    token_data = token_file.content.decode()
    token_json = json.loads(token_data)
    access_token = token_json['access_token']

    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token

    send_values = {
        "touser": user,    #企业号中的用户帐号，如果配置不正常，将按部门发送。
        "toparty": sectionid,    #企业号中的部门id，如果企业应用对多个部门可见，但是这里只添一个部门也只对这个部门可见。
        "msgtype": "text", #消息类型。
        "agentid": agentid,    #企业号中的应用id。
        "text": {
            "content": subject + '\n' + content
           },
        "safe": "0"
        }
    send_data = json.dumps(send_values)
    print(send_url)
    print(send_data)
    try:
        send_request = requests.post(send_url, send_data)
    except Exception as e:
        print(e)


@app.route("/rds", methods=['GET', 'POST', 'PUT'])
def rds_alarm():
    alarm_data = eval(request.data.decode())
    subject = alarm_data["Subject"]
    content_json = {"event_start_time":alarm_data["Timestamp"]}
    content = str(content_json)
    corpsecret = "h-Qp68VswECRlIUAIi6ELDMFnb0fVifilNgCclnIxWs"
    user = "3"
    sectionid = "3"
    agentid = "1000006"
    senddata(corpsecret, user, sectionid, agentid, subject, content)
    return "200"

@app.route("/redis", methods=['GET', 'POST', 'PUT'])
def redis_alarm():
    alarm_data = eval(request.data.decode())
    subject = alarm_data["Subject"]
    content_json = {"event_start_time":alarm_data["Timestamp"]}
    content = str(content_json)
    corpsecret = "QDWVpn6EhQj_yvruTn2ksjQvftBDXbCYLUVfMaL1RVM"
    user = "3"
    sectionid = "3"
    agentid = "1000007"
    senddata(corpsecret, user, sectionid, agentid, subject, content)
    return "200"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
