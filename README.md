# 通用应用监控框架

@author Danny0

监控应用并将数据保存到influxdb中, 目前已经实现Redis/Mysql/Nginx监控。
[influxdb 官方安装文档](http://docs.influxdata.com/influxdb/v1.2/introduction/installation/)

# 使用

## 基础配置

首先在代码中添加influxdb的连接配置:
```
influx_config = {
    "host": "127.0.0.1",
    "port": 8086,
    "username": "",
    "password": "",
    "database": ""
}
```

## Redis监控
设置redis连接的配置信息：
```
redis_config = {
    "host": "127.0.0.1",
    "password": "",
    "port": 
}
```
引入监控类并实例化: 
```
from monflux import RedisMonitor
RedisMonitor(influx_config, redis_config, "redis_load").start()
```
第三个参数是influxdb保存的measurement

注：需要安装python redis客户端库，可通过`pip install redis`安装

## Mysql监控

设置Mysql连接的配置信息：
```
mysql_config = {
    "host": "127.0.0.1",
    "username": "",
    "password": "",
    "port": 3306
}
```

引入监控类并实例化: 
```
from monflux import MysqlMonitor
MysqlMonitor(influx_config, mysql_config, "mysql_load").start()
```
注：需要安装python mysql客户端库，可通过`pip install mysql-python`安装

## Nginx监控

设置Nginx的配置信息：
```
nginx_config = {
    "url": "http://10.110.95.67/nginx_status",
}
```

引入监控类并实例化: 
```
from monflux import NginxMonitor
NginxMonitor(influx_config, nginx_config, "nginx_load").start()
```

## 其他
您可以参考Redis或者Nginx的监控实现来写您自己的插件。  
具体教程待补充。

# 数据展现

可通过Grafana来展示保存到influxdb中的监控数据。
mysql配置示例：
![](http://img.peablog.com/2017-06-13-14973476197412.jpg)

mysql监控展示效果：
![](http://img.peablog.com/2017-06-13-14973477306458.jpg)

您还可以通过influxdata自家的Chronograf来展示，毕竟是influxdata自家的东西，对influxdb的支持应该要好一些。

# 类似工具
influxdb的开发商influxdata旗下本身已有一款监控工具：Telegraf. 它不仅支持自家的influxdb, 也支持Es、Kafka等其他流行开源工具, 支持的输入插件也非常多。
但它的使用方式是通过配置文件来实现的，部分配置感觉略复杂。
