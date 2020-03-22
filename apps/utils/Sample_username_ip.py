# -*- coding: utf-8 -*-
# @Time    :2020/3/19 17:51
import logging

logger = logging.getLogger("django")


def ip_username(request):

    logger.error(request.user.username)

    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
        logger.error(ip)
    else:
        ip = request.META['REMOTE_ADDR']
        logger.error(ip)

