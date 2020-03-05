from rest_framework import serializers

from .models import Role, Menu, User


class RoleSerializer(serializers.ModelSerializer):
    # # 自动向内部进行深度查询  depth表示查询层数
    class Meta:
        model = Role
        # fields = "__all__"
        fields = ['id', 'code', 'name']
        # depth = 1  # 0 ~ 10  默认的depth为0

    # id = serializers.CharField()
    # name = serializers.CharField()
    # code = serializers.CharField()


class MenuSerializer(serializers.ModelSerializer):
    # # 自动向内部进行深度查询  depth表示查询层数
    class Meta:
        model = Menu
        fields = ['id', 'parent_id', 'name', 'code', 'type', 'layer']


class UserSerializer(serializers.ModelSerializer):
    # # 自动向内部进行深度查询  depth表示查询层数
    user_type = serializers.CharField(source='get_user_type_display')

    class Meta:
        model = User
        fields = ['id', 'username', 'user_type', 'head', 'email', 'mobile', 'status']
