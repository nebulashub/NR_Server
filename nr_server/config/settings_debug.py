# 调试环境 配置文件

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nr_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3307'
    }
}

REDIS_SERVER = "reds://127.0.0.1:6379/1"
