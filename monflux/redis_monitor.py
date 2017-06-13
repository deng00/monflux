#!encoding=utf-8
__author__ = 'peablog'
import redis
from monitor import Monitor


class RedisMonitor(Monitor):
    need_config_fields = ["host", "port", "password"]

    def init(self):
        self.ins = redis.Redis(self.app_config.host, self.app_config.port, 0, self.app_config.password)

    def get_tag(self):
        return {
            "host": self.app_config.host
        }

    def get_data(self, fields):
        info = self.ins.info()
        data = {
            "used_memory": info["used_memory"] / (1024 * 1024),
            "used_memory_percent": info["used_memory"] * 100 / info["total_system_memory"],
            "connected_clients": info["connected_clients"],
            "instantaneous_ops_per_sec": info["instantaneous_ops_per_sec"]
        }
        return data
