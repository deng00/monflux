#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Danny0'
from monflux.redis_monitor import RedisMonitor
from monflux.mysql_monitor import MysqlMonitor
from monflux.nginx_monitor import NginxMonitor

if __name__ == "__main__":
    influx_config = {
        "host": "127.0.0.1",
        "port": 8086,
        "username": "",
        "password": "",
        "database": ""
    }
    redis_config = {
        "host": "127.0.0.1",
        "password": "",
        "port": 6379
    }
    RedisMonitor(influx_config, redis_config, "redis_load").start()
    mysql_config = {
        "host": "127.0.0.1",
        "username": "",
        "password": "",
        "port": 3306
    }
    MysqlMonitor(influx_config, mysql_config, "mysql_load").start()
    nginx_config = {
        "url": "http://127.0.0.1/nginx_status",
    }
    NginxMonitor(influx_config, nginx_config, "nginx_load").start()
