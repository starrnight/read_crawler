# -*- coding: utf-8 -*-
# @Filename    : superset_gunicorn.conf.py.py
# @Date        : 2021-10-28 16:54
# @Description : 
# @Author      : hexin
# @Version     : V 0.1.0
# @Remark      :

# -*- coding: utf-8 -*-
from multiprocessing import cpu_count

# bind = ["0.0.0.0:8078"]

# 是否开启守护进程模式
daemon = False

# 保存gunicorn的进程pid的文件
# pidfile = 'gunicorn.pid'

# 工作进程数量
# workers = cpu_count() * 2 + 1
workers = cpu_count()

# worker_class = "gevent"  # 指定一个异步处理的库
# 比 gevent 更快的一个异步网络库
# worker_class = "egg:meinheld#gunicorn_worker"

# 单个进程的最大连接数
worker_connections = 2000

# 服务器保持连接的时间，能够避免频繁的三次握手过程
keepalive = 60

# 一个请求的超时时间
timeout = 600
# 重启时限
graceful_timeout = 10
# 允许哪些ip地址来访问
forwarded_allow_ips = '*'

"""
日志处理
"""
# 是否捕获输出
capture_output = True
# 日志级别
# loglevel = 'error'
# 错误日志存储路径
# errorlog = 'log/superset_error.log'
