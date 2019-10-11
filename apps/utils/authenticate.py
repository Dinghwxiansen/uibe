from datetime import datetime

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


from apps.base import models


class MyAuthenticate(BaseAuthentication):

    """认证用户是否已经登录类"""
    """添加自己的认证逻辑，基类BaseAuthentication中有两个必须要重写的接口"""
    def authenticate(self, request):
        # todo:获取token参数
        token = request.query_params.get('token')
        if not token:
            token = request.META.get("HTTP_TOKEN")
        token_obj = models.UserToken.objects.filter(token=token).first()  # 在数据库UserToken查找是否有相应的对象
        if not token_obj:  # 如果没有，则跑出异常

            raise exceptions.AuthenticationFailed("用户认证失败")
        elif (token_obj.expr < datetime.now()):

            raise exceptions.AuthenticationFailed("token过期")
        return (token_obj.user, token_obj)  # 这里需要返回两个对象，分别是UserInfo对象和UserToken对象

    def authenticate_header(self, request):  # 返回相应头信息
        pass
