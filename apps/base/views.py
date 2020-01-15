from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework import mixins

from apps.utils import restful
from apps.utils.pagination import Pagination
from .filter import RoleFilter, UserFilter
from .models import User, Role, Menu
from .serializer import RoleSerializer, MenuSerializer, UserSerializer

"""
权限模块相关操作

"""


class RoleView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, ):
    """
    角色列表页
    """
    # 定义分页类
    # pagination_class = Pagination
    authentication_classes = []
    queryset = Role.objects.all().order_by("-update_time")
    # 序列化
    serializer_class = RoleSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # 设置filter的类为我们自定义的类
    filter_class = RoleFilter
    # 搜索，前端通过search关键字传值，？search=''
    search_fields = ('=code', '=name')  # 在这里添加可以搜索的字段，=表示等， 还可使用正则
    # 排序
    # ordering_fields = ('create_time', )

    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        添加角色,并返回添加的数据
    """

    def post(self, request, *args, **kwargs):

        try:
            ret = self.create(request, *args, **kwargs)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        删除
    """

    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(request, *args, **kwargs)
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        查询一条数据详情
    """

    def patch(self, request, id):
        ret = Role.objects.filter(pk=id).first()
        ser = RoleSerializer(instance=ret, many=False)
        return restful.result(data=ser.data)

    """
        更新单条数据
    """

    def put(self, request, *args, **kwargs):
        # print(request.data)
        try:
            # self.partial_update(request, *args, **kwargs)
            ret = Role.objects.filter(id=request.data['id']).first()
            ser = RoleSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


"""
菜单操作类
"""


class MenuView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, generics.GenericAPIView, ):
    queryset = Menu.objects.all().order_by("order_num")
    # 序列化
    serializer_class = MenuSerializer

    lookup_field = 'id'

    """
        查询列表
    """

    def get(self, request, *args, **kwargs):
        print(request.user.username)
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        添加菜单,并返回添加的数据
    """

    def post(self, request, *args, **kwargs):
        print(request.data)
        try:
            # 判断是否为一级菜单,parent_id为0标识一级菜单
            if request.data["parent_id"] == 0:
                # 查询编码值最大的一级菜单，设置以及菜单的编码和排序字段
                firstLevelMenu = Menu.objects.filter(parent_id=0).order_by("-code").first()
                # print(connection.queries)
                if firstLevelMenu:
                    code_num = int(firstLevelMenu.code) + 1
                    code = "%03d" % code_num
                    order_num = firstLevelMenu.order_num + 5
                else:
                    code = "001"
                    order_num = 1
                request.data["code"] = code
                request.data["order_num"] = order_num
                request.data["layer"] = 1
                print(code)
                print(order_num)
            else:
                # 查询父级菜单
                parentNenu = Menu.objects.get(id=request.data["parent_id"])
                # 其他层级的菜单，查询同一个父亲的菜单
                brotherMenu = Menu.objects.filter(parent_id=parentNenu.id).order_by("-code").first()
                if brotherMenu:
                    code_num = int(brotherMenu.code[-3:]) + 1
                    code = brotherMenu.code[:-3] + "%03d" % code_num
                    order_num = brotherMenu.order_num + 5
                else:
                    code = parentNenu.code + "001"
                    order_num = 1
                request.data["code"] = code
                request.data["order_num"] = order_num
                request.data["layer"] = parentNenu.layer + 1
            request.data["perms"] = request.data["code"]
            ret = self.create(request, *args, **kwargs)
            # return restful.result(message="保存成功",data=ret.data)
            return restful.result(message="保存成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        删除
    """

    def delete(self, request, *args, id):
        try:
            self.destroy(request, *args, id)
            print(id)
            print(Menu.objects.filter(parent_id=id))
            Menu.objects.filter(parent_id=id).delete()

            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        查询一条数据详情
    """

    def patch(self, request, id):
        print(id)
        ret = Menu.objects.filter(pk=id).first()
        ser = MenuSerializer(instance=ret, many=False)
        return restful.result(message="查询成功", data=ser.data)

    """
        更新单条数据
    """

    def put(self, request):
        print(request.data)
        try:
            ret = Menu.objects.get(pk=request.data['id'])
            # partial=True 标识局部跟新
            ser = MenuSerializer(instance=ret, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
            return restful.ok()
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)


class UserView(mixins.ListModelMixin, generics.GenericAPIView, ):
    queryset = User.objects.all().order_by("username")
    # 序列化
    serializer_class = UserSerializer
    # 定义分页类
    pagination_class = Pagination

    lookup_field = 'id'

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # 设置filter的类为我们自定义的类
    filter_class = UserFilter

    """
        查询列表
    """

    def get(self, request, *args, **kwargs):
        # todo 创建用户
        # User.objects.create_user("dading","1")
        try:
            ret = self.list(request, *args, **kwargs)
            return restful.result(message="操作成功", data=ret.data)
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        查询一条数据详情
    """

    def patch(self, request, id):
        ret = User.objects.filter(pk=id).first()
        ser = UserSerializer(instance=ret, many=False)
        return restful.result(message="查询成功", data=ser.data)


class UserRoleView(mixins.ListModelMixin, generics.GenericAPIView, ):
    """
    设置用户角色
    """
    # 序列化
    serializer_class = RoleSerializer

    def post(self, request, *args, **kwargs):
        try:
            # eavl 将字符串转换为列表

            if "," in request.data["role_id"]:
                roles = Role.objects.filter(id__in=eval(request.data["role_id"]))
            else:
                roles = Role.objects.filter(id=request.data["role_id"])

            if "," in request.data["user_id"]:
                users = User.objects.filter(id__in=eval(request.data["user_id"]))

            else:
                users = User.objects.filter(id=request.data["user_id"])

            for user in users:
                # 设置角色之前，先查询当前用户对应的所有角色，进行删除，然后在插入。
                user.role.set([])  # 删除
                user.role.set(roles)  # 插入
            return restful.result(message="操作成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        查询指定用户的所有角色
    """

    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            roles = user.role.all()
            # todo 判断查询条件查询数据库是否为空
            if roles.exists():
                ser = RoleSerializer(instance=roles, many=True)
                return restful.result(message="查询成功", data=ser.data)
            else:
                return restful.result(message="查询成功，当前用户无角色，请为用户添加角色")
        except Exception as e:
            return restful.result2(message="查询失败,id传输错误", data=e.args)


class RoleMenuView(mixins.ListModelMixin, generics.GenericAPIView, ):
    """
    设置角色菜单
    """
    # 序列化
    serializer_class = MenuSerializer

    def post(self, request, *args, **kwargs):
        try:
            # eavl 将字符串转换为列表

            if "," in request.data["role_id"]:
                roles = Role.objects.filter(id__in=eval(request.data["role_id"]))
            else:
                roles = Role.objects.filter(id=request.data["role_id"])

            if "," in request.data["menu_id"]:
                menus = Menu.objects.filter(id__in=eval(request.data["menu_id"]))

            else:
                menus = Menu.objects.filter(id=request.data["menu_id"])

            for role in roles:
                # 设置权限之前，先查询当前角色对应的所有权限，进行删除，然后在插入。
                role.menu.set([])  # 删除
                role.menu.set(menus)  # 插入
            return restful.result(message="操作成功")
        except Exception as e:
            return restful.result2(message="操作失败", data=e.args)

    """
        查询指定角色的所有菜单
    """

    def get(self, request, role_id):
        try:
            role = Role.objects.get(pk=role_id)
            menus = role.menu.all()
            # todo 判断当前查询条件是否为空
            if menus.exists():
                ser = MenuSerializer(instance=menus, many=True)
                return restful.result(message="查询成功", data=ser.data)
            else:
                return restful.result(message="查询成功，当前角色无菜单")
        except Exception as e:
            return restful.result(message="role_id传入错误，请检查", data=e.args)


class UserMenuView(mixins.ListModelMixin, generics.GenericAPIView, ):
    """
    查询指定用户对应的菜单，如果没有传递user_id参数，表示查当前登录用户的所有菜单
    """
    # 序列化
    serializer_class = MenuSerializer

    def get(self, request):
        user_id = request.GET.get("user_id")
        if not user_id:
            user_id = request.user.id

        menus = Menu.objects.filter(roles__users__id=user_id).distinct()
        ser = MenuSerializer(instance=menus, many=True)
        return restful.result(message="查询成功", data=ser.data)
