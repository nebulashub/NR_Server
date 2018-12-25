import zlib

from google.protobuf.json_format import MessageToDict

from framework.autowired import Service, autowired
from framework.util.time import DateTime
from nr_server.common.cache import NRRedisCache

from nr_server.common.logger import NRLogger
from nr_server.common.platform import Platform
from nr_server.data.models.eth_market_value import EthMarketValueModel
from nr_server.data.models.eth_nr_by_addr import EthNrByAddrModel
from nr_server.data.models.eth_nr_by_date import EthNrByDateModel
from nr_server.data.models.eth_nr_total import EthNrTotalModel
from nr_server.data.models.neb_market_value import NebMarketValueModel
from nr_server.data.models.neb_nr_by_addr import NebNrByAddrModel
import nr_server.data.proto.nr_data_pb2 as pb
from nr_server.data.models.neb_nr_by_date import NebNrByDateModel
from nr_server.data.models.neb_nr_total import NebNrTotalModel


@Service()
class NRDataSource(object):
    """
    nr数据源
    """
    _logger: NRLogger = autowired(NRLogger)
    _cache = NRRedisCache

    def get_daily_nr(self, platform: Platform, date: str) -> list:
        """
        返回某一天所有地址的nr数据
        :param platform: 平台
        :param date: 日期. 格式："20180601"
        :return: Nr数据数组
        """
        model = EthNrByDateModel
        if platform == Platform.Nebulas:
            model = NebNrByDateModel

        r = self._cache.get(self._daily_key(platform, date))
        if r is not None:
            return r
        ls = model.objects.filter(date=DateTime.from_str(date, '%Y%m%d', timezone_hours=0).timestamp)
        if ls is not None and len(ls) > 0:
            s = zlib.decompress(ls[0].data)
            r = MessageToDict(pb.Data().FromString(s))['items']
            self._cache.set(self._daily_key(platform, date), r)
        else:
            r = []
        return r

    def get_address_nr(self, platform: Platform, address: str) -> list:
        """
        返回某一地址的所有nr数据
        :param platform: 平台
        :param address: 地址
        :return: Nr数据数组
        """
        model = EthNrByAddrModel
        if platform == Platform.Nebulas:
            model = NebNrByAddrModel

        r = self._cache.get(self._address_key(platform, address))
        if r is not None:
            return r
        ls = model.objects.filter(address=address)
        if ls is not None and len(ls) > 0:
            d = ls[0].data
            a = d.split(b'|')
            items = []
            for pb_item in a:
                items.append(MessageToDict(pb.Item().FromString(pb_item)))
            r = items
            self._cache.set(self._address_key(platform, address), r)
        else:
            r = []
        return r

    def get_market_value_histories(self, platform: Platform):
        """
        返回所有市值历史记录
        :param platform:
        :return:
        """
        model = EthMarketValueModel
        if platform == Platform.Nebulas:
            model = NebMarketValueModel
        r = self._cache.get(self._market_key(platform))
        if r is not None:
            return r
        r = list(model.objects.all().values())
        if r is not None and len(r) > 0:
            self._cache.set(self._market_key(platform), r)
        return r

    def get_total_nr_histories(self, platform: Platform):
        """
        返回所有Nr值历史记录
        :param platform:
        :return:
        """
        model = EthNrTotalModel
        if platform == Platform.Nebulas:
            model = NebNrTotalModel
        r = self._cache.get(self._nr_total_key(platform))
        if r is not None:
            return r
        r = list(model.objects.all().values())
        if r is not None and len(r) > 0:
            self._cache.set(self._nr_total_key(platform), r)
        return r

    def get_random_address(self, platform: Platform):
        """
        返回有值地址
        :param platform:
        :return:
        """
        model = EthNrByAddrModel
        if platform == Platform.Nebulas:
            model = NebNrByAddrModel
        r = self._cache.get(self._random_addresses_key(platform))
        if r is not None:
            return r
        r = list(model.objects.filter(last_above_0_num__gt=0).order_by('-last_above_0_num')[0: 20])
        d = []
        if r is not None and len(r) > 0:
            for m in r:
                d.append(m.address)
            self._cache.set(self._random_addresses_key(platform), d)
        return d

    # private ----------------------------------------------------------------------------------------------------------

    @staticmethod
    def _daily_key(platform: Platform, date: str) -> str:
        return platform.value + '_' + date

    @staticmethod
    def _address_key(platform: Platform, address: str) -> str:
        return platform.value + '_' + address

    @staticmethod
    def _market_key(platform: Platform) -> str:
        return platform.value + '_market'

    @staticmethod
    def _nr_total_key(platform: Platform) -> str:
        return platform.value + '_nr_total'

    @staticmethod
    def _random_addresses_key(platform: Platform) -> str:
        return platform.value + '_random_addresses'
