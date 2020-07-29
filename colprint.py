
grey = "\x1b[38m"
yellow = "\x1b[33m"
red = "\x1b[31m"
blue = "\x1b[34m"
reset = "\x1b[0m"
cyan = "\x1b[36m"
magenta = "\x1b[35m"

class colprint:
    '''
    Class for colorizing prints
    '''
    def __init__(self):
        pass

    def info(self, msg):
        return print(blue + str(msg) + reset)

    def error(self, msg):
        return print(red + str(msg) + reset)

    def warn(self, msg):
        return print(yellow + str(msg) + reset)

    def response(self, msg):
        return print(cyan + str(msg) + reset)

    def query(self, msg):
        return print(yellow + str(msg) + reset)