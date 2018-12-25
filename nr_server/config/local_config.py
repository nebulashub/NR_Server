import os
import re
from enum import unique, Enum


@unique
class Env(Enum):
    Debug = 0     # 调试环境
    Test = 1      # 测试环境
    Product = 2   # 生产环境


class LocalConfig(object):

    _config_data = None

    @classmethod
    def current_env(cls):
        env = cls.get('env')
        if env == "Debug":
            return Env.Debug
        elif env == "Test":
            return Env.Test
        else:
            return Env.Product

    @classmethod
    def get(cls, key):
        return cls._configs()[key]

    @classmethod
    def _configs(cls):
        if cls._config_data is None:
            d = os.path.dirname(os.path.abspath(__file__))
            cls._config_data = cls._read(os.path.join(d, 'local.ini'))
        return cls._config_data

    @classmethod
    def _read(cls, path):
        r = dict()
        f = open(path, encoding="utf8")
        for line in f.readlines():
            if re.match(r'^[^=]+=[^=]+$', line):
                i = line.index("=")
                k = line[0:i].strip()
                v = line[i + 1:len(line)].strip()
                r[k] = v
        return r
