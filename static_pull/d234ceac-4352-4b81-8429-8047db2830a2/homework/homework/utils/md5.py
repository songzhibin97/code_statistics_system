import hashlib
from settings import Config

def md5(arg):
    hash = hashlib.md5(Config.SALT)
    hash.update(bytes(arg,encoding='utf-8'))
    return hash.hexdigest()