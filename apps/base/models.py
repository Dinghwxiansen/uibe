# base/models.py
__author__ = 'wuyi'


from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager



"""
    重新定义UserManager：我们还需要定义自己的UserManager
"""
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("请填入用户名！")
        user = self.model(username=username, *extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields['is_superuser'] = True
        return self._create_user(username, password)

status_choices = (
    (True, "启用"),
    (False, "停用"),
)

"""
用户信息
"""
class User(AbstractBaseUser,PermissionsMixin):
    user_type_choices =(
        (1,"教职工"),
        (2,"本科生"),
        (3,"研究生"),
    )
    id = models.BigAutoField("id", primary_key=True)
    username = models.CharField("用户名(学号/教职工号/研究生)", unique=True, max_length=150)
    head = models.CharField("头像", max_length=150, null=True)
    user_type = models.IntegerField("用户类型", choices=user_type_choices, default=1)
    email = models.EmailField("邮箱",max_length=128, null=True)
    mobile = models.CharField("手机号",max_length=32, null=True)
    status = models.BooleanField("状态", choices=status_choices, default=True)
    create_time = models.DateTimeField("创建时间", auto_now=True)
    update_time = models.DateTimeField("修改时间", auto_now_add=True)
    role = models.ManyToManyField("Role",related_name="users", verbose_name="角色id")


    USERNAME_FIELD = 'username'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        # db_table = 'base_user'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        # 设置权限
        permissions=()
        #设置索引
        # unique_together = ("username",)


"""
角色表 base_role
"""
class Role(models.Model):
    id = models.BigAutoField("id", primary_key=True)
    name = models.CharField("名称",max_length=128)
    code = models.CharField("编码",max_length=128)
    # user = models.ManyToManyField("User", related_name="user", verbose_name="用户id")
    menu = models.ManyToManyField("Menu", related_name="roles",verbose_name="菜单Id")
    create_time = models.DateTimeField("创建时间", auto_now=True)
    update_time = models.DateTimeField("修改时间", auto_now_add=True)
    class Meta:
        verbose_name = "角色信息表"
        verbose_name_plural = verbose_name


"""
菜单表 base_menu
"""
class Menu(models.Model):
    menu_type_choices = (
        (0, "目录"),
        (1, "菜单"),
        (2, "按钮"),
    )

    id = models.BigAutoField("id", primary_key=True)
    # parent = models.ForeignKey("Menu",on_delete=models.CASCADE,default=0,verbose_name="父Id")
    parent_id = models.BigIntegerField("父Id",default=0)
    name = models.CharField("名称",max_length=128)

    code = models.CharField("编码",max_length=128,default=0)
    perms = models.CharField("权限", max_length=128)
    layer = models.IntegerField("层级", default=1)
    order_num = models.IntegerField("排序", default=1)

    url = models.CharField("地址",max_length=128,null=True,blank=True)
    type = models.IntegerField("类型", choices=menu_type_choices, default=0)
    icon = models.CharField("图标", max_length=256,null=True)
    status = models.BooleanField("状态", choices=status_choices, default=True)
    create_time = models.DateTimeField("创建时间",auto_now=True)
    update_time = models.DateTimeField("修改时间",auto_now_add=True)


    class Meta:
        verbose_name = "菜单信息表"
        verbose_name_plural = verbose_name
        permissions=()
        ordering=[
            'order_num'
        ]

"""
token表
"""
class UserToken(models.Model):
    # id = models.BigAutoField("id", primary_key=True)
    user = models.OneToOneField("User", on_delete=models.CASCADE, primary_key=True)
    token = models.CharField("token", max_length=64)
    expr = models.DateTimeField("token到期时间")

    class Meta:
        db_table = "base_user_token"
        verbose_name = "token表"
        verbose_name_plural = verbose_name
