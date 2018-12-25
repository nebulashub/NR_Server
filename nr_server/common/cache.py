from django.conf import settings
from django_redis.cache import RedisCache

from framework.util.json import JsonUtil


REDIS_DEFAULT_TIMEOUT = 60


class NRRedisCache(object):

    _redis: RedisCache = RedisCache(settings.REDIS_SERVER, {})

    @classmethod
    def get(cls, key, default_value=None, timeout=REDIS_DEFAULT_TIMEOUT):
        return cls._redis.get_or_set(key, default=default_value, timeout=timeout)

    @classmethod
    def get_from_json(cls, key, default_value=None, timeout=REDIS_DEFAULT_TIMEOUT):
        r = cls._redis.get_or_set(key, default=default_value, timeout=timeout)
        if r is not None:
            r = JsonUtil.deserialize(r)
        return r

    @classmethod
    def set(cls, key, data, timeout=REDIS_DEFAULT_TIMEOUT):
        cls._redis.set(key, data, timeout=timeout)

    @classmethod
    def set_to_json(cls, key, data, timeout=REDIS_DEFAULT_TIMEOUT):
        cls._redis.set(key, JsonUtil.serialize(data), timeout=timeout)

    @classmethod
    def has_key(cls, key):
        return cls._redis.has_key(key)

    @classmethod
    def expire(cls, key, timeout):
        cls._redis.expire(key, timeout)

    @classmethod
    def ttl(cls, key):
        return cls._redis.ttl(key)


class NRLocalMemCache(object):

    _data = dict()

    @classmethod
    def get(cls, key):
        if key in cls._data.keys():
            return cls._data[key]
        else:
            return None

    @classmethod
    def set(cls, key, value):
        if value is None:
            if key in cls._data.keys():
                cls._data.pop(key)
        else:
            cls._data[key] = value
