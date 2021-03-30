import redis


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RedisInstance(metaclass=Singleton):

    def __init__(self, host, port, password, db=0):
        self.client = redis.StrictRedis(host=host, port=port,
                                        db=db, password=password, decode_responses=True)
        self.client.ping()

    def get(self, key):
        return self.client.get(key)

    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        return self.client.set(name, value, ex, px, nx, xx)

    def setnx(self, name, value):
        return self.client.setnx(name, value)

    def sadd(self, name, value):
        return self.client.sadd(name, value)

    def is_member(self, name, value):
        return self.client.sismember(name, value)

    def smember(self, name):
        return self.client.smembers(name)

    def hgetall(self, name):
        return self.client.hgetall(name)

    def hexists(self, name, key):
        return self.client.hexists(name, key)

    def hset(self, name, key, value):
        return self.client.hset(name, key, value)
