#!/usr/bin/python3

# Download readings from the humidity and temperature meter

import requests
import time
import elitech
from datetime import datetime
import json


class DataReaderRecord:
    def __init__(self, record_nr, record_date, temp, humidity):
        self._record_nr = record_nr
        self._record_date = record_date
        self._temp = temp
        self._humidity = humidity

    def record_nr(self):
        return self._record_nr

    def record_date(self):
        return self._record_date

    def record_ts(self):
        return int(datetime.timestamp(self._record_date))

    def temp(self):
        return self._temp

    def humidity(self):
        return self._humidity


class DataReader:
    def __init__(self):
        self._device = elitech.Device("/dev/ttyUSB0")  # Raspberry Pi
        self._device.init()
        self._devinfo = self._device.get_devinfo()
        self._data_reader_records = []
        print(self._devinfo)
        print("User info: {}".format(self._devinfo.user_info))
        print("Number of records: {}".format(self._devinfo.rec_count))

        body = self._device.get_data()
        # print("Body: {}".format(body))
        for item_tuple in body:
            drr = DataReaderRecord(*item_tuple)  # type = DataReaderRecord
            self._data_reader_records.append({'temp': drr.temp(), 'humidity': drr.humidity(),
                                              'recordnr': drr.record_nr(), 'recordts': drr.record_ts()})
        print(self._data_reader_records)

    def set_reader_interval(self, hours, minutes, seconds):

        param_put = self._devinfo.to_param_put()  # convert devinfo to parameter
        param_put.rec_interval = datetime.time(hours, minutes, seconds)    # update parameter
        param_put.stop_button = elitech.StopButton.ENABLE   # update parameter
        param_put_res = self._device.update(param_put)    # update device

    def get_records(self):
        return self._data_reader_records

    def get_latest_record(self):
        return self._data_reader_records[len(self._data_reader_records) - 1]

    def get_json(self):
        return json.dumps(self.get_records())


if __name__ == "__main__":

    dr = DataReader()
    ldr = dr.get_latest_record()
    print("Latest entry {}: {} = {}C and {}% (timestamp: {})".format(datetime.fromtimestamp(ldr['recordts']),
                                                                     ldr['recordnr'],
                                                                     ldr['temp'], ldr['humidity'],
                                                                     ldr['recordts']))

    url = 'https://yourserver.com/uploadDataReaderData'
    payload = {'data_reader_json': dr.get_json()}
    r = requests.post(url, data=payload)
    print(r.text)
