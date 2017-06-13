#!encoding=utf-8
import time

__author__ = 'peablog'

from abc import ABCMeta, abstractmethod
from influxdb import InfluxDBClient
from dotmap import DotMap
import threading
from monitor_exception import MonitorConfigException


class Monitor(threading.Thread):
    __metaclass__ = ABCMeta

    # app config need fields
    need_config_fields = []

    def __init__(self, influx_config, app_config, measurement):
        threading.Thread.__init__(self)
        self.check_config(influx_config, ["host", "port", "username", "password", "database"])
        self.influx_config = DotMap(influx_config)
        self.check_config(app_config, self.need_config_fields)
        self.app_config = DotMap(app_config)
        self.measurement = measurement
        self.init()
        self.db = InfluxDBClient(self.influx_config.host, self.influx_config.port, self.influx_config.username,
                                 self.influx_config.password, self.influx_config.database)

    @abstractmethod
    def init(self):
        """
        can do some init work here
        :return:
        """
        pass

    @abstractmethod
    def get_data(self, fields):
        """
        get monflux data
        :param fields:
        :return:
        """
        pass

    @abstractmethod
    def get_tag(self):
        """
        get tags
        :return:
        """
        pass

    @staticmethod
    def check_config(config, fields):
        """
        check config filed
        :param config:
        :param fields:
        :return:
        """
        for field in fields:
            if field not in config:
                raise MonitorConfigException("field not set: " + field)

    def run(self, fields=None):
        """
        get and save current monflux data
        :param fields:
        :return:
        """
        if fields is None:
            fields = []
        points_data = [
            {
                "measurement": self.measurement,
                "tags": self.get_tag(),
                "fields": self.get_data(fields)
            }
        ]
        self.db.write_points(points_data)
