from framework.autowired import autowired
from framework.mvc.controller import Controller
from framework.mvc.decorator import JsonApi
from nr_server.common.platform import Platform
from nr_server.data.nr_data_source import NRDataSource


class NRApiController(Controller):
    """
    NR相关restful api由此类提供
    """

    _data: NRDataSource = autowired(NRDataSource)

    @JsonApi
    def daily_all_nr(self, date):
        return self._data.get_daily_nr(Platform.Nebulas, date)

    @JsonApi
    def address_nr(self, address):
        return self._data.get_address_nr(Platform.Nebulas, address)
