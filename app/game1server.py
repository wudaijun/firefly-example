from firefly.server.globalobject import GlobalObject, remoteserviceHandle

@remoteserviceHandle("gate")
def game1Handle(data):
    print "game1Handle: ", data
    return "game1Handle completed"
