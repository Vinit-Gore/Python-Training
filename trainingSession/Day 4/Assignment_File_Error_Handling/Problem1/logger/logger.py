def LogInfo(msg):
    try:
        with open('logger\example.log', 'a') as fd:
            fd.writelines('\nINFO: ' + msg)
    except IOError:
        print("Could not log info")


def LogError(msg):
    try:
        with open('logger\example.log', 'a') as fd:
            fd.writelines('\nERROR: ' + msg)
    except IOError:
        print("Could not log error")
