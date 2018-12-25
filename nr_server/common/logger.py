import logging

from django.http import HttpRequest, HttpResponse

from framework.autowired import Component
from framework.mvc.logger import ReqLogger


@Component()
class NRLogger(ReqLogger):

    def __init__(self):
        self._all_logger = logging.getLogger('all')
        self._req_logger = logging.getLogger('req')
        self._ero_logger = logging.getLogger('ero')
        self._dbg_logger = logging.getLogger('dbg')
        ReqLogger.set_logger(self)

    def log(self, msg):
        self._all_logger.info(msg)

    def log_req_info(self, info):
        self._req_logger.info(info)

    def log_err(self, ero):
        self._ero_logger.error(ero)

    # 重写ReqLogger
    def write_req_info(self, req: HttpRequest, resp: HttpResponse):
        msg = req.get_raw_uri() + " method: " + req.method
        if req.method == "POST":
            if req.body is not None:
                msg += " body: " + req.body.decode("utf-8")
        content = str(resp.content)
        content_len = len(content)
        if len(content) > 300:
            content = content[0: 300] + " ..."
        msg += " resp(" + str(content_len) + "): " + content
        self.log_req_info(msg)

    # 重写ReqLogger
    def write_api_log(self, msg):
        self.log_req_info(msg)

    # 重写ReqLogger
    def write_ero_log(self, error):
        self.log_err(error)
