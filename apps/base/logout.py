
from rest_framework.views import APIView

from apps.utils import restful
from django.contrib.auth import get_user_model,logout
from .models import UserToken


User = get_user_model()
"""
登出,清楚session，
"""
class LogoutView(APIView):

    def get(self,request):
        try:
            # 删除当前用户对应的token
            UserToken.objects.get(user_id=request.user.id).delete()
            # 调用django的登出方法
            logout(request)
            return restful.result("登出成功")
        except Exception as e:
            print(e)
            return restful.server_error_500("系统错误！")

