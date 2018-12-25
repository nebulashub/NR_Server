from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from framework.mvc.logger import ReqLogger


class Controller(View):

    ctrl = None

    def get(self, req, *args, **kwargs):
        return self._do_req(req, *args, **kwargs)

    def post(self, req, *args, **kwargs):
        return self._do_req(req, *args, **kwargs)

    def _do_req(self, req, *args, **kwargs):
        f = getattr(self, self.ctrl)
        resp = f(self, *args, **kwargs)
        ReqLogger._log_req_info(req, resp)
        return resp

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Controller, self).dispatch(*args, **kwargs)

    def body(self):
        if self.request.body is not None:
            return self.request.body.decode("utf-8")
        return None

    def post_param(self, key):
        if self.request.POST is not None:
            return self.request.POST.get(key, default=None)

    def get_param(self, key):
        if self.request.GET is not None:
            return self.request.GET.get(key, default=None)

    def header_param(self, key):
        key = key.replace("-", "_").upper()
        if not "".startswith("HTTP_"):
            key = "HTTP_" + key
        if key in self.request.META:
            return self.request.META.get(key)
        return None

    def param(self, key):
        p = self.get_param(key)
        if p is None:
            p = self.post_param(key)
        if p is None:
            p = self.header_param(key)
        return p

    def headers(self):
        return {k: v for k, v in self.request.META.items() if k.startswith("HTTP_")}
