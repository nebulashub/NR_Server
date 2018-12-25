from abc import abstractmethod


class ReqLogger(object):

    _logger = None

    @abstractmethod
    def write_req_info(self, req, resp):
        pass

    @abstractmethod
    def write_api_log(self, msg):
        pass

    @abstractmethod
    def write_ero_log(self, error):
        pass

    @classmethod
    def set_logger(cls, logger):
        if not isinstance(logger, ReqLogger):
            raise Exception("logger is not an instance of ReqLogger")
        cls._logger = logger

    @classmethod
    def _log_req_info(cls, req, resp):
        if cls._logger is not None:
            cls._logger.write_req_info(req, resp)

    @classmethod
    def _log_api_msg(cls, msg):
        if cls._logger is not None:
            cls._logger.write_api_log(msg)

    @classmethod
    def _log_error(cls, error):
        if cls._logger is not None:
            cls._logger.write_ero_log(error)
