# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # author:dingxiansen
# # datetime:2020/9/25 16:22
# # software: PyCharm
#
# from __future__ import absolute_import
#
# import os
# from datetime import datetime, timedelta
#
# from celery import shared_task
# from django.http import HttpResponse
#
# # from system.models import LogVisitTimes, TotalVisitTimes
#
#
# # 函数如果需要传参，那么在celery.py下的定时任务模块中添加args项。
# @shared_task
# def test1(x, y):
#     return x + y
#
#
# @shared_task
# def test2(x):
#     return x
