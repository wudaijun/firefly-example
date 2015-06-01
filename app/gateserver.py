#coding:utf-8

from firefly.server.globalobject import GlobalObject, rootserviceHandle


@rootserviceHandle
def gateHandle1(data):
    print "gateHandle: ", data
    return "gateHandle Completed"

@rootserviceHandle
def gateHandle2(data):
    print "gateHandle2: ", data, "forward to game1: "
    # 通过callChild调用指定孩子节点上的函数
    return GlobalObject().root.callChild("game1", "game1Handle", data)

