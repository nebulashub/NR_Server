from django.http import HttpResponse

from ..util.json import JsonUtil


class ApiResult(object):

    code = 0
    data = None
    msg = ""

    def __init__(self, code, data, msg):
        self.code = code
        self.data = data
        self.msg = msg

    @staticmethod
    def r(data):
        return ApiResult(0, data, "")

    @staticmethod
    def e(msg, code=-1):
        return ApiResult(code, None, msg)


class JsonApiResponse(HttpResponse):

    def __init__(self, data):
        HttpResponse.__init__(
            self,
            JsonUtil.serialize(data),
            content_type="application/json; charset=utf8"
        )
