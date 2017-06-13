#!encoding=utf-8
__author__ = 'peablog'

import time
import requests
import urlparse
from monitor import Monitor


class NginxMonitor(Monitor):
    need_config_fields = ["url"]

    def init(self):
        pass

    def get_tag(self):
        url = urlparse.urlparse(self.app_config.url)
        return {
            "host": url.netloc
        }

    def get_status(self):
        res = requests.get(self.app_config.url)
        text = res.text.split("\n")
        total = str(text[2]).strip().split(" ")
        num = text[3].split(" ")
        status = {
            "active_connections": int(text[0].split(": ")[1]),
            "num_connection": int(total[0]),
            "num_handshake": int(total[1]),
            "num_request": int(total[2]),
            "reading": int(num[1]),
            "writing": int(num[3]),
            "waiting": int(num[5])
        }
        return status

    def get_data(self, fields):
        status1 = self.get_status()
        time.sleep(3)
        status2 = self.get_status()
        return {
            "active_connections": status2["active_connections"],
            "num_connection": (status2["num_connection"] - status1["num_connection"]) / 3,
            "num_handshake": (status2["num_handshake"] - status1["num_handshake"]) / 3,
            "num_request": (status2["num_request"] - status1["num_request"]) / 3,
            "reading": status2["reading"],
            "writing": status2["writing"],
            "waiting": status2["waiting"]
        }
