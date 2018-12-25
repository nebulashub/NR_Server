from framework.autowired import autowired
from framework.mvc.api import ApiResult
from framework.mvc.controller import Controller
from framework.mvc.decorator import JsonApi
from framework.util.time import DateTime
from nr_server.common.platform import Platform
from nr_server.data.nr_data_source import NRDataSource


class NRDemoController(Controller):
    _data: NRDataSource = autowired(NRDataSource)
    _LAST_DAYS = 7

    @JsonApi
    def nr_and_market_value(self, platform: str, begin: str, end: str):
        b = DateTime.from_str(begin, '%Y%m%d', timezone_hours=0).timestamp
        e = DateTime.from_str(end, '%Y%m%d', timezone_hours=0).timestamp
        all_market_value = self._data.get_market_value_histories(Platform.from_value(platform))
        mv = []
        for m in all_market_value:
            if b <= m['date'] < e:
                mv.append(m)
        all_nr_value = self._data.get_total_nr_histories(Platform.from_value(platform))
        nv = []
        for n in all_nr_value:
            if b <= n['date'] < e:
                nv.append(n)
        return {"market": mv, "nr": nv}

    @JsonApi
    def daily_high_score(self, platform: str, date: str, num: str):
        num = int(num)
        d = self._data.get_daily_nr(Platform.from_value(platform), date)
        if len(d) > num:
            return d[0: num]
        else:
            return d

    @JsonApi
    def address_info(self, platform: str, address: str):
        dt = DateTime(timezone_hours=0).add_days(-1).date.timestamp
        data: list = self._data.get_address_nr(Platform.from_value(platform), address)

        current = None
        last = None
        last_seven_days = []

        c = len(data)
        if c > 0:
            for i in range(c):
                t = data[c - i - 1]
                if float(t['score']) > 0:
                    last = t
                    break
            if last is None:
                last = data[c - 1]
            cdt = DateTime.from_str(data[c - 1]["date"], '%Y%m%d', timezone_hours=0).timestamp
            if cdt == dt:
                current = data[c - 1]

        if c > self._LAST_DAYS:
            ds = data[c - self._LAST_DAYS: c]
        else:
            ds = data

        def find(lds, date):
            for d in lds:
                if d['date'] == DateTime(date, timezone_hours=0).to_str('%Y%m%d'):
                    return d
            return None

        for i in range(self._LAST_DAYS):
            dt = DateTime(timezone_hours=0).add_days(i - self._LAST_DAYS).timestamp
            last_seven_days.append([dt, find(ds, dt)])

        return {
            "current": current,
            "last": last,
            "lastSevenDays": last_seven_days
        }

    @JsonApi
    def random_addresses(self, platform: str):
        return self._data.get_random_address(Platform.from_value(platform))
