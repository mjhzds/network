import pandas as pd
import math


def processIp(row, col):
    ip = data.loc[row, col]
    elements = ip.split(".")
    result = 0
    for element in elements:
        num = int(element)
        for i in range(0, elements.index(element)):
            num += num*num
        result += num
    result = math.log(result)
    data.loc[row, col] = result


def processLevel(row, col):
    levels = {
        '轻微': 2, "信息": 1, '一般': 3, '重要': 4
    }
    level = levels.get(data.loc[row, col])
    data.loc[row, col] = level


def processType(row, col):
    types = {
        '/安全预警': 2, '/操作记录': 1, '/操作记录/软件维护': 1, '/攻击入侵/漏洞利用': 3, '/认证授权/安全认证': 4,
        '/认证授权/账号管理': 4, '/网络访问': 5, '/网络访问/会话连接': 5, '/网络访问/正常访问': 5, '/系统状态': 6,
        '/信息刺探/网络扫描': 7
    }
    type = types.get(data.loc[row, col])
    data.loc[row, col] = type


def processDevice(row, col):
    types = {
        '/安全设备/防火墙': 1, '/网络设备/负载均衡': 2, '/安全设备/Web应用安全网关': 3, '/安全设备/VPN': 4, '/安全设备/安全管理平台': 5,
        '/安全设备/堡垒机': 6, '/安全设备/上网行为审计': 7, '/网络设备/交换机': 8, '/中间件/Nginx': 9
    }
    type = types.get(data.loc[row, col])
    data.loc[row, col] = type


def processResponse(row, col):
    responses = {
        '丢弃': 1, '拒绝': 2, '无响应': 3, '允许': 4
    }
    response = responses.get(data.loc[row, col])
    data.loc[row, col] = response


def processContent(row, col):
    contents = {
        'TCP': 1, 'UDP': 2, 'ICMP': 3, 'null': 4
    }
    content = str(data.loc[row, col])
    res = {}
    protocol = ''
    for l in content.split(' '):
        c = l.split('=')
        if len(c) == 2:
            res[c[0]] = c[1]
    if 'Protocol' not in res:
        protocol = 'null'
    else:
        protocol = res['Protocol']
    data.loc[row, col] = contents.get(protocol)


if __name__ == '__main__':
    data = pd.read_csv("event_utf8.csv")
    data.dropna(axis=0, inplace=True)
    data.drop(labels='事件接收时间', axis=1, inplace=True)
    data.drop(labels='设备名称', axis=1, inplace=True)

    for i in data["事件类型"].index:
        processLevel(i, '事件等级')
        processType(i, '事件类型')
        processIp(i, '设备IP地址')
        processDevice(i, '设备类型')
        processIp(i, '源IP地址')
        processIp(i, '目的IP地址')
        processResponse(i, '响应')
        processContent(i, '事件原始内容')

    # data = (data - data.min()) / (data.max() - data.min())
    data.to_csv("process.csv")