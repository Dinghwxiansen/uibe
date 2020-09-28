#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dingxiansen
# datetime:2020/9/25 16:17
# software: PyCharm

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from celery.schedules import crontab
from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uibe.settings')

app = Celery('uibe')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

# 允许root 用户运行celery
platforms.C_FORCE_ROOT = True

# 以下是定时任务模块，可以添加一个或多个定时任务， 如只是部署异步任务，可以把这段代码注释掉
app.conf.update(
    CELERYBEAT_SCHEDULE={
        'test1': {
            'task': 'portrait.tasks.test1',  # 这个task任务在app下的tasks.py文件内
            'schedule': timedelta(seconds=10),
            # 'args': （想传的参数）#不传参也可去除此项
        },
        '任务名称（自定义）': {
            'task': '你的项目app.tasks.你要执行的脚本或代码函数',  # 这个task任务在app下的tasks.py文件内
            'schedule': crontab(hour=1, minute=5),
            # 'args': （想传的参数）#不传参也可去除此项
        }
    }
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
