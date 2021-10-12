#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gunicorn Configuration File."""
import multiprocessing


bind = "0.0.0.0:80"



proc_name = "NCSSLAB"
daemon = True
timeout = 300


workers = multiprocessing.cpu_count()
worker_class = "gthread"
threads = 2


capture_output = True
errorlog = "log/gunicorn_error.log"
accesslog = 'log/gunicorn_access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
