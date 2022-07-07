import logging
from pprint import pprint
import sys
import time
import datetime
import os
import json
from datadog import initialize, statsd
from ddtrace import config, patch_all, Pin, patch, tracer
import functools

config.env = "dev"      # the environment the application is in
config.service = "flask-server"  # name of your application
config.version = "0.0.1"  # version of your application
import logging
logging.basicConfig()
patch_all()


@tracer.wrap("assemble_sandwich", service="my-sandwich-making-svc", resource="resource_name")
def send_metrics():
    statsd.gauge('python.example_metric.type', 0, tags=["alert:true", "x_service:a"])
    statsd.gauge('python.example_metric.depth', 20, tags=["alert:true", "x_service:a", "test"])


while(1):
    send_metrics()
    print("hi here we are ")
    time.sleep(7)