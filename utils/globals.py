
# Тут происходит безумие с метаклассами
# Полезное на почитать - https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

# И окей, это пока не понадобилось
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ForwardMessage(metaclass=Singleton):
    _from_user: str
    _text: str
    
    def __init__(self, text: str = '', from_user: str = ""):
        self._from_user: str = from_user
        self._text: str = text
    
    @classmethod
    def set_message(cls, text: str = '', from_user: str = ""):
        instance = cls()
        instance._from_user = from_user
        instance._text = text
    
    
    @classmethod
    def add_message(cls, text: str = '', from_user: str = ""):
        instance = cls()
        if instance._from_user == '':
            instance._from_user = from_user
        elif instance._from_user == from_user:
            pass
        else:
            instance._from_user = 'from_someone'
        instance._text += '\n' + text

    @classmethod
    def get_from_user(cls):
        return cls()._from_user

    @classmethod
    def get_text(cls):
        return cls()._text