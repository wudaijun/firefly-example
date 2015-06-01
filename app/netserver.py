#coding:utf8

from firefly.server.globalobject import GlobalObject, netserviceHandle

"""
netservice 默认是 CommandService:
    netservice = services.CommandService("netservice")  [位于server/server.py]
    CommandService 的消息响应函数格式为: HandleName_CommandID(conn, data)
    CommandService 会通过'_'解析出CommandID并注册HandleName_CommandId为其消息响应函数
"""

@netserviceHandle
def netHandle_100(_conn, data):
    print "netHandle_100: ", data
    return "netHandle_100 completed"

@netserviceHandle
def netHandle_200(_conn, data):
    print "netHandle_200: ", data, "forward to gate"
    return GlobalObject().remote['gate'].callRemote('gateHandle1', data)

@netserviceHandle
def netHandle_300(_conn, data):
    print "netHandle_300: ", data, "forward to gate"
    return GlobalObject().remote['gate'].callRemote('gateHandle2', data)



