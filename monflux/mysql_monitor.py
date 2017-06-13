#!encoding=utf-8
__author__ = 'peablog'

import time
import MySQLdb
import MySQLdb.cursors
from monitor import Monitor
from monitor_exception import MonitorConfigException


class MysqlMonitor(Monitor):
    need_config_fields = ["host", "port", "username", "password"]

    def init(self):
        try:
            conn = MySQLdb.connect(host=self.app_config.host, user=self.app_config.username,
                                   passwd=self.app_config.password, port=self.app_config.port,
                                   cursorclass=MySQLdb.cursors.DictCursor)
            self.ins = conn.cursor()
        except MySQLdb.Error as e:
            raise MonitorConfigException(e.args[1])

    def get_tag(self):
        return {
            "host": self.app_config.host
        }

    def row2dic(self, rows):
        d = {}
        for r in rows:
            d[r["Variable_name"]] = r["Value"]
        return d

    def query(self, sql):
        self.ins.execute(sql)
        return self.ins.fetchall()

    def get_data(self, fields):
        info1 = self.row2dic(self.query("show global status"))
        time.sleep(3)
        info2 = self.row2dic(self.query("show global status"))
        data = {}
        data["Queries"] = (int(info2["Queries"]) - int(info1["Queries"])) / 3
        data["KBytes_sent"] = (int(info2["Bytes_sent"]) - int(info1["Bytes_sent"])) / (3 * 1024)
        data["Innodb_data_writes"] = (int(info2["Innodb_data_writes"]) - int(info1["Innodb_data_writes"])) / 3
        data["Connections"] = (int(info2["Connections"]) - int(info1["Connections"])) / 3
        data["Threads_connected"] = int(info2["Threads_connected"])
        return data
