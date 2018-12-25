# 测试环境 配置文件

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nr_db',
        'USER': 'root',
        'PASSWORD': 'nebulas.io',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

REDIS_SERVER = "reds://127.0.0.1:6379/1"
