class MyError(object):
    @staticmethod
    def require(condition: bool, message: str = ""):
        if not condition:
            raise Exception(message)

    @staticmethod
    def fail(message: str = ""):
        raise Exception(message)
