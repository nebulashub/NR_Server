from framework.autowired import autowired, Service
from nr_server.common.logger import NRLogger


@Service()
class App(object):
    _logger: NRLogger = autowired(NRLogger)

    def __init__(self):
        pass

    def launch(self):
        self._logger.log('app launch')
        pass
