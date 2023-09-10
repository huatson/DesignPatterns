"""
QUESTIONABLE Object Creation Patterns in Python
https://www.youtube.com/watch?v=Rm4JP7JfsKY
"""

class Singleton(type):
    """METACLASS"""
    _intances = {}

    # as a contructor, will check if the called class (MyLogger)
    # exists already in instances,
    # if not exist, add it and return it,
    # if it exists, just return it,
    # that way we make sure that there is a SINGLE instance of
    # that object always
    def __call__(cls, *args, **kwargs):
        if not cls in cls._intances:
            cls._intances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._intances[cls]


class MyLogger(metaclass=Singleton):
    def log(self, msg):
        print(msg)


logger = MyLogger()
logger.log("logger1")

logger2 = MyLogger()
logger.log("logger2")

# both created objects uses the same instance address
print(hex(id(logger)))
print(hex(id(logger2)))
