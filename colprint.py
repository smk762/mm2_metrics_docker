
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
    def info(self):
        return print(blue + str(self) + reset)

    def error(self):
        return print(red + str(self) + reset)

    def warn(self):
        return print(yellow + str(self) + reset)

    def response(self):
        return print(cyan + str(self) + reset)

    def query(self):
        return print(yellow + str(self) + reset)