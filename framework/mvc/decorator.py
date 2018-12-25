from abc import abstractmethod
from inspect import isfunction
from .api import ApiResult
from .api import JsonApiResponse

from framework.mvc.logger import ReqLogger


class ApiDecoratorBase(object):

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        data = None
        error = None
        try:
            data = self._func(*args, **kwargs)
        except Exception as e:
            ReqLogger._log_error("controller: " + self._func_full_name() + " error: " + repr(e))  # repr(e)
            error = e
        r = self._result(data, error)
        return r

    @abstractmethod
    def _result(self, data, error):
        """此方法由子类实现, 将对象 转换为api要求的数据格式如json或者xml
        :param data:数据对象
        :return:子类转换后的目标格式数据的Response
        """
        pass

    def _func_full_name(self):
        if isfunction(self._func):
            return self._func.__module__ + "." + self._func.__name__
        else:
            return self._func.__module__ + "." + self._func.__class__.__name__


class JsonApi(ApiDecoratorBase):

    def _result(self, data, error):
        """重写父类方法 将数据包装为JsonApiResponse
        :param data:对象数据
        :return:JsonApiResponse
        """
        if error is not None:
            return JsonApiResponse(ApiResult.e("server error"))
        else:
            if not isinstance(data, ApiResult):
                data = ApiResult.r(data)
            return JsonApiResponse(data)
