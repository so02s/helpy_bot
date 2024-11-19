
# Тут происходит безумие с метаклассами
# Полезное на почитать - https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

# И окей, это пока не понадобилось
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Globals(metaclass=Singleton):
    def __init__(self):
        self.agh: str = ""