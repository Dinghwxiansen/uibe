
from django.http import JsonResponse
from rest_framework.views import APIView
from django.db.models import Q

from apps.base import models as base_model
from apps.utils import restful
from django.contrib.auth import get_user_model,authenticate,login
import datetime,json
from apps.utils import constant
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect


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
class LoginView(APIView):
    """
    登录
    """
    #定义权限认证类
    authentication_classes = []

    def post(self,request):
        # self.dispatch()
        try:
            username = request.data['username']
            pwd = request.data['password']
            user = authenticate(request, username=username, password=pwd)
            if user.check_password(pwd):
                login(request, user)
            else:
                return restful.params_error_400("用户名和密码不对")
            # 为用户创建token
            token = md5(user.username)
            # 创建获取时间
            expr = time_add_min(constant.TOKEN_EXPR_MIN)
            # 存在就更新，不存在就创建
            base_model.UserToken.objects.update_or_create(user=user, defaults={'token': token,'expr':expr})
            ret = {'token': token,'expr':expr}
            return restful.result(message="登录成功",data=ret)
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