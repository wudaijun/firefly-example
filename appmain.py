#coding:utf8
"""
本模块在启动master时作为参数传入
firefly会在每个Server(除了master)启动时都调用该模块:
    cmds = 'python %s %s %s'%(self.mainpath, sername, self.configpath) [位于master/master.py, 其中self.mainpath即为本模块] 
"""
import os
import json, sys
from firefly.server.server import FFServer

if __name__ == '__main__':
    args = sys.argv
    servername = None
    config = None
    if len(args) > 2:
        servername = servername = args[1]
        config = json.load(open(args[2], 'r'))
    else:
        raise ValueError

    dbconf = config.get('db', {})
    memconf = config.get('memcached', {})
    servsconf = config.get('servers', {})
    masterconf = config.get('master',{})
    serverconf = servsconf.get(servername)
    server = FFServer()
    server.config(serverconf, dbconfig=dbconf, memconfig=memconf, masterconf=masterconf)
    print servername, 'start'
    server.start()
    print servername, 'stop'
