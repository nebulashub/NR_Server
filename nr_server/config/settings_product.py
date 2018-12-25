# 生产环境 配置文件

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'neb_rank',
        'USER': 'eco_wallet',
        'PASSWORD': 'oGWSLIqVvQRR4r4ItGLc',
        'HOST': 'nebulas.cvajxeo2mhiu.us-west-1.rds.amazonaws.com',
        'PORT': '3306'
    }
}

REDIS_SERVER = "reds://127.0.0.1:6379/1"
