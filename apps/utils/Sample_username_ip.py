# -*- coding: utf-8 -*-
# @Time    :2020/3/19 17:51
import logging
import time
import datetime

logger = logging.getLogger("django")

# 日志记录登录人ip和username
def ip_username(request):

    logger.error(request.user.username)

    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
        logger.error(ip)
    else:
        ip = request.META['REMOTE_ADDR']
        logger.error(ip)
# 比较时间大小
def time_cmp(first_time, second_time):
    date_time = datetime.datetime.strptime(first_time, '%Y-%m-%d')
    date_time2 = datetime.datetime.strptime(second_time, '%Y-%m-%d')
    return int(time.mktime(date_time.timetuple()))-int(time.mktime(date_time2.timetuple()))


#    return datetime.strptime(first_time,"%Y-%m-%d")


