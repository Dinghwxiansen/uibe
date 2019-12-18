# -*- coding: utf-8 -*-
# @Time    :2019/8/26 11:00
from rest_framework import serializers

from apps.portrait import models as pm
from apps.warning import models as wm

"""*********************下拉列表序列化*******************"""


class YxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.Yx
        fields = ['code', 'name']


class NjSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.Nj
        fields = ['code', 'name', 'p_yx']


class BjSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.Bj
        fields = ['code', 'name', 'p_nj']


"""********************本专科生序列化******************"""


class BzksSerialiser(serializers.ModelSerializer):
    yjcs = serializers.IntegerField()  # 自定义显示字段

    # ct = serializers.DateField(source='')

    class Meta:
        model = pm.UibeBzks
        # fields = '__all__'
        fields = ['xh', 'xm', 'yx', 'xznj', 'bj', 'fdy', 'yjcs']
    #
    # def get_yjcs(self, row):
    #     cs = row.yjcs.all()
    #     ret = []
    #     for item in cs:
    #         ret.append({'id': item.id})
    #     return ret.__len__()


"""*****************************在籍在校不选课明细序列化-*****************"""


class ZjzxbxkmxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.ZnyjZjzxbxk
        fields = ['id', 'xh', 'yjrq', 'sjxf', 'yxxf', 'wxkxq', 'clzt', ]


"""**********************休学退学不离校明细序列化*******************************"""


class XxtxblxMxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.ZnyjXxtxblx
        fields = ['id', 'xh', 'yjrq', 'txxx', 'yjqk', 'yjdj', 'clzt', ]


"""*******************************校外住宿序列化*******************************"""


class XwzsMxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.ZnyjXwzsyj
        fields = ['id', 'xh', 'yjrq', 'xwzsts', 'yjqk', 'yjdj', 'clzt', ]


"""*******************************不在校预警序列化*******************************"""


class BzxMxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.ZnyjBzx
        fields = ['id', 'xh', 'yjrq', 'bzxsj', 'bzxsc', 'yjdj', 'clzt', ]


"""*******************************逃课行为预警序列化*******************************"""


class TkxwMxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.ZnyjTkxw
        fields = ['id', 'xh', 'yjrq', 'kcsd', 'kcmc', 'yjqk', 'clzt', ]


"""*******************************晚归预警序列化*******************************"""


class WgMxSerialiser(serializers.ModelSerializer):
    ycqk = serializers.CharField(source="get_yjqk_display")

    class Meta:
        model = wm.ZnyjWgyj
        fields = ['id', 'xh', 'yjsj', 'wgsj', 'ycqk', 'yjdj', 'clzt', ]


"""*******************************上网行为预警序列化*******************************"""


class BzksSwxwSerialiser(serializers.ModelSerializer):
    zsyll = serializers.FloatField()  # 自定义显示字段，总使用流量

    class Meta:
        model = pm.UibeBzks
        fields = ['xh', 'xm', 'yx', 'xznj', 'bj', 'fdy', 'zsyll', ]


class SwxwMxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.ZnyjSwxw
        fields = ['id', 'xh', 'syll', 'create_time', 'swsj']


"""*******************************行为轨迹序列化*******************************"""

# """行为轨迹预警序列化"""
#
#
# class XwgjSerialiser(serializers.ModelSerializer):
#     # yjcs = serializers.SerializerMethodField()  # 自定义显示字段
#
#     class Meta:
#         model = models.UibeBzks
#         # fields = '__all__'
#         fields = ['id', 'xm', 'yx', 'xznj', 'bj', 'fdy', 'create_time', 'yjcs']


"""下拉列表序列化"""


# 这个序列化器就是展示地区名
class SpinnerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.Spinner
        fields = ('id', 'yxbj',)


# 这个序列器展示下一个
class NextSpinnerInfoSerializer(serializers.ModelSerializer):
    # 嵌套关系
    addinfo = SpinnerInfoSerializer(many=True, read_only=True)

    # 注意 这里的    addinfo 要和 上面 models.py 文件里的related_name 名字相对应
    # addinfo = serializers.StringRelatedField(many=True, read_only=True)
    # 这个是返回字符串显示的是__str__方法返回的内容。
    # 上面什么都不写，也就是只有下面Meta类的时候，默认是PrimaryKeyrelatedField，也就是显示id
    #  显示下一级的内容
    class Meta:
        model = wm.Spinner
        fields = ('id', 'yxbj', 'addinfo',)


"""系统管理之假期设置序列化"""


class JqSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XtglJq
        fields = ['id', 'jqmc', 'jqkssj', 'jqjssj', 'jqms', 'kqzt', ]


"""系统管理之标签维度序列化"""


class BqwdSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XtglBqwd
        fields = ['id', 'wdmc', 'wdms', 'create_time', 'kqzt']


"""系统管理之指标项管理序列化"""


class ZbxglSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XtglZbx
        fields = ['id', 'zbxmc', 'zbfl', 'zbwd', 'zdxz', 'jsgz', 'sjzb_id', 'create_time', 'zbms', 'kqzt', ]


"""系统管理之画像标签设置序列化"""


class BqszSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XtglBqsz
        fields = ['id', 'bqmc', 'zbfl', 'zbwd', 'create_time', 'zbx', 'bqgz', 'bqms', 'kfqx', 'kqzt']


"""画像标签设置之新增选择指标项"""


class HxbqszZbxSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XtglZbx
        fields = ['id', 'zbxmc', 'zbwd', 'kqzt']


"""预警阈值设置之在籍在校不选课修改序列化"""


class XtglYjyzszZjzxbxkSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjmc', 'yjms', 'yjgz', 'kqzt']


"""预警阈值设置之逃课行为预警修改序列化"""


class TkxwxgSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjmc', 'yjms', 'yjgz', 'kqzt']


"""预警阈值设置之晚归预警修改序列化"""


class WgxgSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjgz', 'yjmc', 'yjms', 'kqzt', 'red', 'yellow', 'orange']


"""预警阈值设置之休学退学不离校预警修改序列化"""


class XxtxblxxgSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjgz', 'yjmc', 'yjms', 'kqzt', 'red', 'yellow', 'orange']


"""预警阈值设置之校外住宿预警修改序列化"""


class XwzsxgSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjgz', 'yjmc', 'yjms', 'kqzt', 'red', 'yellow', 'orange']


"""预警阈值设置之不在校预警修改序列化"""


class BzxSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'yjmc', 'yjms', 'kqzt', 'red', 'yellow', 'orange', 'code', 'yjgz']


"""预警阈值设置序列化"""


class YjyzszSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjmc', 'yjms', 'yjgz', 'kqzt']


"""预警阈值设置历史记录序列化"""


class YjyzlsszSerializer(serializers.ModelSerializer):
    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjmc', 'yjgz', 'yjms', 'update_time']


"""指标项管理之数据库选择"""


class SjbxzSerializer(serializers.ModelSerializer):
    # sjzb_id = serializers.SerializerMethodField()  # 自定义显示字段

    class Meta:
        model = pm.Sjzb
        fields = ['id', 'zwbm', 'ywbm']


class SjbxzzdSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.Sjzbzd
        fields = ['id', 'ywbm', 'sjzb_id', 'zwzdmc', 'zdsjbbs', 'sjlx', 'bz']


#  自定义序列化字段
class SjzbzdSerializer2(serializers.Serializer):
    # 字段必须与数据库里面的字段一样
    id = serializers.IntegerField()
    zwzdmc = serializers.CharField()
    zdsjbbs = serializers.CharField()
    sjlx = serializers.CharField()
    bz = serializers.CharField()
    sjzb_id = serializers.IntegerField()


"""教师画像"""


class UibeJzgSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeJzg
        fields = ['id', 'zgh', 'xm', 'bm']


"""教师画像管理员下拉列表bm"""


class UibeJzgBmSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.JzgBm
        fields = ['bmdm', 'bm']


"""教师画像详情"""


class UibeJzgXqSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeJzg
        fields = ['id', 'zgh', 'xm', 'xb', 'csrq', 'xw', 'xl', 'lxrq', 'zzmm', 'jsjzs', 'jszgz', 'gqpxzs', 'qtzs',
                  'yjfx',
                  'zxxmsl', 'hxxmsl', 'cgjlsl', 'yjbgsl', 'zzcgsl', 'lwcgsl', 'bm', 'rylb', 'gwzj', 'zcjb', 'xngw',
                  'zxsf', 'jl', 'yjskcxsrc', 'yjskcskjc', 'yjskcxss', 'yjskcskms', 'bkkcxsrc', 'bkkcskjc', 'bkkcxss',
                  'bkkcskms', 'tsjycs', 'ekxf', 'wlsyll', 'wlsysc']


"""教师画像职称详情"""


class UibeJzgZcXqSerializer(serializers.ModelSerializer):
    # tjzc_nums = serializers.SerializerMethodField()
    # bbmzc_nums = serializers.SerializerMethodField()

    class Meta:
        model = pm.JzgZcxx
        fields = ['zwdm', 'zwmc', 'zwjb']


"""用户画像之学生画像教师端"""


class XshxJstSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeBzks
        fields = ['xh', 'xm', 'yx', 'xznj', 'bj']


"""用户画像之学生画像教师端详情"""


class XshxJstXqSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XshxBq
        fields = ['bq', 'bqsm', 'bqqx', ]


"""*******************************行为轨迹序列化*******************************"""


class BzksXwgjSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeBzks
        fields = ['xh', 'xm', 'yx', 'xznj', 'bj', 'fdy', ]


class XwgjMxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.XwgjGrgj
        fields = ['id', 'xh', 'xwsj', 'xwdd', 'jd', 'wd', ]
