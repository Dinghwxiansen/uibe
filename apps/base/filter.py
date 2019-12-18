import django_filters

from apps.base.models import Role, User
from apps.portrait import models as pm
from apps.warning import models as wm


class RoleFilter(django_filters.FilterSet):
    class Meta():
        model = Role
        fields = ["id", "code", "name"]

        # # 两个参数，name是要过滤的字段，lookup是执行的行为，‘小与等于本店价格’icontains表示模糊搜索
        # price_min = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
        # price_max = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
        #
        # class Meta:
        #     model = Goods
        #     fields = ['price_min', 'price_max']


class UserFilter(django_filters.FilterSet):
    class Meta():
        model = User
        fields = ["username"]


class BzksFilter(django_filters.FilterSet):
    class Meta:
        model = pm.UibeBzks
        fields = ['yx', 'xznj', 'bj', 'xslb', 'xjzt', 'sfxx', 'sftx', 'jg', 'sfsqxwzs', ]


"""********************************在籍在校不选课明细*************************"""


class ZjzxbxkmxFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')

    class Meta:
        model = wm.ZnyjZjzxbxk
        fields = ['xh', 'kssj', 'jssj', 'clzt']


"""********************************休学退学不离校明细*************************"""


class XxtxblxmxFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')

    class Meta():
        model = wm.ZnyjXxtxblx
        fields = ['xh', 'yjdj', 'kssj', 'jssj', 'clzt']


"""********************************校外住宿明细*************************"""


class XwzsmxFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')

    class Meta():
        model = wm.ZnyjXwzsyj
        fields = ['xh', 'yjdj', 'kssj', 'jssj', 'clzt']


"""*******************************不在校明细*************************"""


class BzxmxFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')

    class Meta():
        model = wm.ZnyjBzx
        fields = ['xh', 'yjdj', 'kssj', 'jssj', 'clzt']


"""********************************逃课行为明细*************************"""


class TkxwmxFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')

    class Meta():
        model = wm.ZnyjTkxw
        fields = ['xh', 'kssj', 'jssj', 'clzt']


"""********************************晚归明细*************************"""


class WgmxFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')

    class Meta():
        model = wm.ZnyjWgyj
        fields = ['xh', 'kssj', 'jssj', 'yjdj', 'clzt', 'yjqk', ]


"""********************************上网行为明细*************************"""


class SwxwmxFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')
    xm = django_filters.CharFilter(field_name="xm", lookup_expr='icontains')

    class Meta():
        model = wm.ZnyjSwxw
        fields = ['xh', 'kssj', 'jssj', 'syll', ]


# """在籍在校不选课过滤"""
# from apps.warning.models import UibeBzks
#
#
# class BzksFilter(django_filters.FilterSet):
#     # min = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
#     # max = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')
#
#     class Meta():
#         model = UibeBzks
#         fields = ['xm', 'xh', 'yx', 'xznj', 'bj']
#
# """在籍在校不选课明细过滤"""
# from apps.warning.models import ZnyjZjzxbxk
#
#
# class BzksmxFilter(django_filters.FilterSet):
#     min = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
#     max = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')
#
#     class Meta():
#         model = ZnyjZjzxbxk
#         fields = ['clzt', 'min', 'max']


"""系统管理之假期设置"""


class JqFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')
    jqmc = django_filters.CharFilter(field_name="jqmc", lookup_expr='icontains')

    class Meta():
        model = pm.XtglJq
        fields = ['jqmc', 'kssj', 'jssj']


"""系统管理之标签维度管理"""


class BqwdFilter(django_filters.FilterSet):
    wdmc = django_filters.CharFilter(field_name="wdmc", lookup_expr='icontains')

    class Meta():
        model = pm.XtglBqwd
        fields = ['id', 'kqzt', 'wdmc']


"""系统管理之画像标签设置"""


class HxbqszFilter(django_filters.FilterSet):
    class Meta():
        model = pm.XtglBqsz
        fields = ['bqmc']


"""画像标签设置之指标项选择"""


class HxbqszZbxFilter(django_filters.FilterSet):
    zbwd = django_filters.CharFilter(field_name="zbwd", lookup_expr='icontains')

    class Meta():
        model = pm.XtglZbx
        fields = ['zbwd']


"""系统管理之指标项管理"""


class ZbxglFilter(django_filters.FilterSet):
    class Meta():
        model = pm.XtglZbx
        fields = ['zbxmc', 'zbfl']


"""系统管理之预警阈值设置"""


class YjyzsjFilter(django_filters.FilterSet):
    yjmc = django_filters.DateFilter(field_name="yjmc", lookup_expr='icontains')

    class Meta():
        model = wm.XtglYjyzsz
        fields = ['yjmc', 'code']


"""指标项之数据表选择"""


class SjbxzFilter(django_filters.FilterSet):
    class Meta():
        model = pm.Sjzb
        fields = ['zwbm', 'ywbm']


"""指标项之数据表字段选择"""


class SjbxzzdFilter(django_filters.FilterSet):
    class Meta():
        model = pm.Sjzbzd
        fields = ['sjzb_id', 'zwzdmc']


"""用户画像之教师画像"""


class UibeJzgFilter(django_filters.FilterSet):
    xm = django_filters.CharFilter(field_name="xm", lookup_expr='icontains')

    class Meta():
        model = pm.UibeJzg
        fields = ['xm', 'zgh', 'bm']


"""用户画像之学生画像教师端"""


class XshxJsdFilter(django_filters.FilterSet):
    xm = django_filters.DateFilter(field_name="xm", lookup_expr='icontains')

    class Meta():
        model = pm.UibeBzks
        fields = ['xm', 'xh', 'yx', 'xznj', 'bj']


"""用户画像之学生画像教师端详情过滤"""


class XshxJsdXqFilter(django_filters.FilterSet):
    class Meta():
        model = pm.XshxBq
        fields = ['xh']


"""********************************行为轨迹明细*************************"""


class XwgjmxFilter(django_filters.FilterSet):
    kssj = django_filters.DateFilter(field_name="create_time", lookup_expr='gte')
    jssj = django_filters.DateFilter(field_name="create_time", lookup_expr='lte')

    class Meta():
        model = wm.XwgjGrgj
        fields = ['xh', 'kssj', 'jssj', ]


"""下拉列表过滤"""


class YxFilter(django_filters.FilterSet):
    class Meta:
        model = wm.Yx
        fields = ['code']


class NjFilter(django_filters.FilterSet):
    class Meta:
        model = wm.Nj
        fields = ['code', 'p_yx']


class BjFilter(django_filters.FilterSet):
    class Meta:
        model = wm.Bj
        fields = ['code', 'p_nj']
