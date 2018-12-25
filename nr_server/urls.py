"""nr_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url

from framework.autowired import autowired
from nr_server.common.app import App
from nr_server.controller.nr_api_controller import NRApiController
from nr_server.controller.nr_demo_controller import NRDemoController

urlpatterns = [
    # api --------------------------------------------------------------------------------------------------------------

    # 返回 Nebulas 某一天所有地址的nr值
    url(r'^api/daily_all_nr/(?P<date>\d{8})/$', NRApiController.as_view(ctrl="daily_all_nr")),

    # 返回 Nebulas 某地址所有日期的nr值
    url(r'^api/address_nr/(?P<address>.+)/$', NRApiController.as_view(ctrl="address_nr")),


    # demo -------------------------------------------------------------------------------------------------------------

    # 返回 某时间段内 eth或者neb nr值和对应的市值
    url(r'^nd/nr_and_market_value/(?P<platform>\w+)/(?P<begin>\d{8})/(?P<end>\d{8})/$',
        NRDemoController.as_view(ctrl="nr_and_market_value")),

    # 返回 eth或者neb 某一天nr值排名前num位的数据
    url(r'^nd/daily_high_score/(?P<platform>\w+)/(?P<date>\d{8})/(?P<num>\d+)/$',
        NRDemoController.as_view(ctrl="daily_high_score")),

    # 查询某地址nr信息
    url(r'^nd/address_info/(?P<platform>\w+)/(?P<address>\w+)/$', NRDemoController.as_view(ctrl="address_info")),

    # 获取随机地址
    url(r'^nd/random_addresses/(?P<platform>\w+)/$', NRDemoController.as_view(ctrl="random_addresses")),
]

# handler500 = "nr_server.error_views._500_view"
# handler400 = "nr_server.error_views._400_view"
# handler404 = "nr_server.error_views._404_view"

app = autowired(App)
app.launch()
