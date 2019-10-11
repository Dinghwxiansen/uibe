# -*- coding: utf-8 -*-
import traceback

from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import (PermissionDenied, AuthenticationFailed, MethodNotAllowed, NotAuthenticated,
                                       PermissionDenied as RestPermissionDenied,
                                       ValidationError)
from rest_framework.response import Response
from rest_framework.views import set_rollback


def exception_handler(exc, content):
    data = {
        'data': None
    }
    if isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
        data = {
            'code': status.HTTP_401_UNAUTHORIZED,
            'message': u'用户未登录或登录态失效，请使用登录链接重新登录',
        }
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    if isinstance(exc, PermissionDenied) or isinstance(exc, RestPermissionDenied):
        message = exc.detail if hasattr(exc, 'detail') else u'该用户没有该权限功能'
        data = {
            'code': status.HTTP_401_UNAUTHORIZED,
            'message': message
        }
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    else:
        if isinstance(exc, ValidationError):
            message = exc.detail if hasattr(exc, 'detail') else u'参数错误'
            data.update({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': message
            })

        elif isinstance(exc, MethodNotAllowed):
            message = exc.detail if hasattr(exc, 'detail') else u'方法不允许访问'
            data.update({
                'code': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': message,
            })

        elif isinstance(exc, Http404):
            # 更改返回的状态为为自定义错误类型的状态码
            message = exc.detail if hasattr(exc, 'detail') else u'404'
            data.update({
                'code': status.HTTP_404_NOT_FOUND,
                'message': message,
            })
        else:
            print(traceback.format_exc())
            # if settings.RUN_MODE != 'PRODUCT':
            #     raise exc
            # 正式环境，屏蔽500
            message = exc.detail if hasattr(exc, 'detail') else u'系统错误'
            data.update({
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': message,
            })

        set_rollback()
        return Response(data, status=status.HTTP_200_OK)

# #这里是字段的 校验
# def validate_fields(data, *fields):
#     """校验必填参数"""
#     validations = []
#     for field in fields:
#         if field not in data:
#             validations.append(u'%s该字段是必填项' % field)
#     if validations:
#         raise ValidationError(validations)
