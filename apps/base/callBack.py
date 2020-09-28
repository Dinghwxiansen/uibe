import datetime

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model, login
from rest_framework.views import APIView

from apps.base import models as base_model
from apps.utils import constant
from apps.utils import restful
import json
from django_cas_ng.views import LoginView as liv, LogoutView as lov
from django.http import HttpRequest, HttpResponse
from django.dispatch import receiver
from django_cas_ng.signals import cas_user_authenticated, cas_user_logout

from apps.utils import restful
from django.contrib.auth import get_user_model, logout
from .models import UserToken

"""
生成token
"""


def md5(user):
    import hashlib
    import time
    # 当前时间，相当于生成一个随机的字符串
    ctime = str(time.time())

    # token加密
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


"""
登录视图
"""
User = get_user_model()


# @method_decorator(csrf_exempt,name="dispatch")
class LoginView(liv):
    """
    登录
    """
    # 定义权限认证类
    authentication_classes = []

    def get(self, request):
        # self.dispatch()

        try:
            username = request.user.get_username()
            # login(request, request.user)
            # 为用户创建token
            token = md5(username)
            # 创建获取时间
            expr = time_add_min(constant.TOKEN_EXPR_MIN)
            # 存在就更新，不存在就创建
            base_model.UserToken.objects.update_or_create(user=request.user, defaults={'token': token, 'expr': expr})
            ret = {'token': token, 'expr': expr}
            return restful.result(message="登录成功", data=ret)
        except Exception as e:
            print(e)
            return restful.server_error_500("系统错误！")


"""
    将当前时间添加分钟，然后返回日期
"""


def time_add_min(minutes):
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=minutes)
    n_days = now + delta
    return n_days.strftime('%Y-%m-%d %H:%M:%S')


@receiver(cas_user_authenticated)
def cas_user_authenticated_callback(sender, **kwargs):
    args = {}
    args.update(kwargs)
    print('''cas_user_authenticated_callback:
    user: %s
    created: %s
    attributes: %s
    ''' % (
        args.get('user'),
        args.get('created'),
        json.dumps(args.get('attributes'), sort_keys=True, indent=2)))


class LogoutView(lov):
    def get(self, request):
        try:
            username = request.user.get_username()
            print(username)
            # 删除当前用户对应的token
            UserToken.objects.get(user_id=request.user.id).delete()
            # 调用django的登出方法
            logout(request)
            return restful.result("登出成功")
        except Exception as e:
            print(e)
            return restful.server_error_500("系统错误！")


# @receiver(cas_user_logout)
# def cas_user_logout_callback(sender, **kwargs):
#     args = {}
#     args.update(kwargs)
#     print('''cas_user_logout_callback:
#     user: %s
#     session: %s
#     ticket: %s
#     ''' % (
#         args.get('user'),
#         args.get('session'),
#         args.get('ticket')))
