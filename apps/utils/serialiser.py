# -*- coding: utf-8 -*-
# @Time    :2019/8/26 11:00
from rest_framework import serializers

from apps.portrait import models as pm
from apps.warning import models as wm
import datetime
import time

"""*********************下拉列表序列化*******************


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
"""


class CollegeSerialiser(serializers.ModelSerializer):
    # yxmc = serializers.CharField(source="get_yxdm_display")

    class Meta:
        model = pm.UibeBzks
        fields = ['yx']
        # depth = 1


class GradeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeBzks
        fields = ['xznj']


class ClassSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeBzks
        fields = ['bj']


class DWSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pm.DW
        fields = ['id', 'yxmc']


"""********************本专科生序列化******************"""


class BzksSerialiser(serializers.ModelSerializer):
    yjcs = serializers.IntegerField()  # 自定义显示字段

    # ct = serializers.DateField(source='')

    class Meta:
        model = pm.UibeBzks
        # fields = '__all__'
        fields = ['xh', 'xm', 'yx', 'xznj', 'bj', 'xjzt', 'syd', 'fdy', 'yjcs']
    #
    # def get_yjcs(self, row):
    #     cs = row.yjcs.all()
    #     ret = []
    #     for item in cs:
    #         ret.append({'id': item.id})
    #     return ret.__len__()


"""*****************************在籍在校不选课明细序列化-*****************"""


class ZjzxbxkmxSerialiser(serializers.ModelSerializer):
    yjrq = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = wm.ZnyjZjzxbxk
        fields = ['id', 'xh', 'yjrq', 'sjxf', 'yxxf', 'wxkxq', 'clzt', ]


"""**********************休学退学不离校明细序列化*******************************"""


class XxtxblxMxSerialiser(serializers.ModelSerializer):
    yjrq = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = wm.ZnyjXxtxblx
        fields = ['id', 'xh', 'yjrq', 'ydrq', 'yjqk', 'yjdj', 'clzt', ]


"""*******************************校外住宿序列化*******************************"""


class XwzsMxSerialiser(serializers.ModelSerializer):
    yjrq = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = wm.ZnyjXwzsyj
        fields = ['id', 'xh', 'yjrq', 'xwzsts', 'yjqk', 'yjdj', 'clzt', ]


"""*******************************不在校预警序列化*******************************"""


class BzxMxSerialiser(serializers.ModelSerializer):
    yjrq = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = wm.ZnyjBzx
        fields = ['id', 'xh', 'yjrq', 'bzxsj', 'bzxsc', 'yjdj', 'clzt', ]


"""*******************************逃课行为预警序列化*******************************"""


class TkxwMxSerialiser(serializers.ModelSerializer):
    yjrq = serializers.DateTimeField(format='%Y-%m-%d')
    yjsj = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = wm.ZnyjTkxw
        fields = ['id', 'xh', 'yjrq', 'kcsd', 'kcmc', 'yjqk', 'yjsj', 'clzt', ]


"""*******************************晚归预警序列化*******************************"""


class WgMxSerialiser(serializers.ModelSerializer):
    yjsj = serializers.DateTimeField(format='%Y-%m-%d')
    wgsj = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = wm.ZnyjWgyj
        fields = ['id', 'xh', 'yjsj', 'wgsj', 'yjqk', 'yjdj', 'clzt', ]


"""*******************************上网行为预警序列化*******************************"""


class BzksSwxwSerialiser(serializers.ModelSerializer):
    zsyll = serializers.FloatField()  # 自定义显示字段，总使用流量

    class Meta:
        model = pm.UibeBzks
        fields = ['xh', 'xm', 'yx', 'xznj', 'bj', 'fdy', 'zsyll', ]


class SwxwMxSerialiser(serializers.ModelSerializer):
    class Meta:
        model = wm.ZnyjSwxw
        fields = ['id', 'xh', 'syll', 'swsj']


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

"""
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
"""

"""系统管理之假期设置序列化"""


class JqSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XtglJq
        fields = ['id', 'jqmc', 'jqkssj', 'jqjssj', 'jqms', 'kqzt', ]


"""系统管理之标签维度序列化"""


class BqwdSerializer(serializers.ModelSerializer):
    # create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = pm.XtglBqwd
        fields = ['id', 'wdmc', 'wdms', 'create_time', 'kqzt']


"""系统管理之指标项管理序列化"""


class ZbxglSerializer(serializers.ModelSerializer):
    # create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = pm.XtglZbx
        fields = ['id', 'zbxmc', 'zbfl', 'zbwd', 'zdxz', 'jsgz', 'sjzb_id', 'create_time', 'zbms', 'kqzt', ]


"""系统管理之画像标签设置序列化"""


# 20200927 添加是否删除字段序列化

class BqszSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XtglBqsz
        fields = ['id', 'bqmc', 'zbfl', 'zbwd', 'create_time', 'zbx', 'bqgz', 'bqSQL', 'bqms', 'bqqx', 'kqzt', 'sfsc', ]


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
        fields = ['id', 'code', 'yjmc', 'yjms', 'yjgz', 'kqzt', 'red', 'yellow', 'orange']


"""预警阈值设置历史记录序列化"""


class YjyzlsszSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjmc', 'yjgz', 'yjms', 'create_time']


class ZjzxbxkYjyzlsszSerializer(serializers.ModelSerializer):
    # create_time = serializers.DateField('create_time')

    create_time = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'yjgz', 'yjms', 'create_time']


class YjyzlsszSerializer2(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = wm.XtglYjyzsz
        fields = ['id', 'code', 'red', 'orange', 'yellow', 'yjgz', 'create_time']


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
        model = pm.UibeJzg
        fields = ['bm']


"""研究生轨迹下拉列表yx"""


class UibeYjsYxSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeYjs
        fields = ['yx']


"""研究生轨迹下拉列表学年"""


class UibeYjsNjSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeYjs
        fields = ['xn']


"""教师画像详情"""
'''
20200927 添加科研信息、教学信息的统计时间
'''


class UibeJzgXqSerializer(serializers.ModelSerializer):
    create_time = serializers.DateField(format='%Y%m%d')
    # lxrq = serializers.DateField(format='%Y-%m-%d')

    # kyxxtjsj = serializers.SerializerMethodField()
    # ekwltjsj = serializers.SerializerMethodField()

    # lxrq = serializers.StringRelatedField(format='%Y-%m-%d')
    wlsysc = serializers.SerializerMethodField()
    wlsyll = serializers.SerializerMethodField()

    class Meta:
        model = pm.UibeJzg
        fields = ['id', 'zgh', 'xm', 'xb', 'csrq', 'xw', 'xl', 'lxrq', 'zzmm', 'jsjzs', 'jszgz', 'gqpxzs', 'qtzs',
                  'yjfx',
                  'zxxmsl', 'hxxmsl', 'cgjlsl', 'yjbgsl', 'zzcgsl', 'lwcgsl', 'bmdm', 'bm', 'rylb', 'gwzj', 'zcxxdm',
                  'zcxx', 'zcbdrq', 'xngw',
                  'zxsf', 'jl', 'yjskcxsrc', 'yjskcskjc', 'yjskcxss', 'yjskcskms', 'bkkcxsrc', 'bkkcskjc', 'bkkcxss',
                  'bkkcskms', 'tsjycs', 'ekxf', 'wlsyll', 'wlsysc', 'create_time', ]

    # def get_kyxxtjsj(self, obj):
    #     lxrq = time.strftime("%Y-%m-%d", obj.lxrq)
    #     create_time = time.strftime("%Y-%m-%d", obj.create_time)
    #     return lxrq + "-" + create_time

    #
    # def get_ekwltjsj(self, obj):
    #     create_time = obj.create_time
    #     tjsj = time.strftime("%Y%m", create_time)
    #     return tjsj

    def get_wlsysc(self, obj):
        sysc = ("%.2f" % float(obj.wlsysc))
        return sysc

    def get_wlsyll(self, obj):
        syll = ("%.2f" % float(obj.wlsyll))
        return syll


"""教师画像职称详情"""


class UibeJzgZcXqSerializer(serializers.ModelSerializer):
    # tjzc_nums = serializers.SerializerMethodField()
    # bbmzc_nums = serializers.SerializerMethodField()

    # class Meta:
    #     model = pm.JzgZcxx
    #     fields = ['zwdm', 'zwmc', 'zwjb']
    ZWPDRQ = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = pm.JzgZcxq
        fields = ['ZWPDRQ', 'ZYJSZWMC', 'ZYJSZWJB']


"""用户画像之学生画像教师端"""


class XshxJstSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeBzks
        fields = ['id', 'xh', 'xm', 'yx', 'xznj', 'bj']


class XtglBqszSerializer(serializers.ModelSerializer):
    class Meta:
        model = pm.XtglBqsz
        fields = ['bqmc', 'bqms', 'bqqx']


# class BqszRelateField(serializers.RelatedField):
#     def to_representation(self, instance):
#         return 'bqmc:%d  bqms:%s' % (instance.bqmc, instance.bqms)


"""用户画像之学生画像教师端详情"""


# class XshxJstXqSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = pm.XshxBq
#         fields = ['bq', 'bqsm']

# todo 20200924 重写学生画像序列化，和model中的bqsz_bqmc相关
class XshxJstXqSerializer(serializers.ModelSerializer):
    # xshxbq = XtglBqszSerializer(many=True, read_only=True, )
    # bqmc = serializers.CharField(source='bq.bqmc', read_only=True)
    # bqms = serializers.CharField(source='bq.bqms', read_only=True)
    # bqqx = serializers.CharField(source='bq.bqqx', read_only=True)
    # bq = BqszRelateField(read_only=True)
    # bq = XtglBqszSerializer(many=True, read_only=True)
    # bq_id = serializers.CharField()

    # 方案一
    bqmc = serializers.ReadOnlyField()
    bqms = serializers.ReadOnlyField()

    # 方案二
    # bqmc = serializers.CharField(source='bq.bqmc')
    # bqms = serializers.CharField(source='bq.bqms')

    class Meta:
        model = pm.XshxBq
        fields = ['bqmc', 'bqms']


"""*******************************本专科生行为轨迹序列化*******************************"""


class BzksXwgjSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeBzks
        fields = ['xh', 'xm', 'yx', 'xznj', 'bj', 'fdy', ]


"""*******************************教职工行为轨迹序列化*******************************"""


class JzgXwgjSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeJzg
        fields = ['zgh', 'xm', 'bm', ]


"""*******************************研究生行为轨迹序列化*******************************"""


class YjsXwgjSerialiser(serializers.ModelSerializer):
    class Meta:
        model = pm.UibeYjs
        fields = ['xh', 'xm', 'yx', 'xn', 'dszgh', ]


"""*******************************本专科生行为轨迹明细序列化*******************************"""


class XwgjMxSerialiser(serializers.ModelSerializer):
    xwsj = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = wm.XwgjGrgj
        fields = ['id', 'xh', 'xwsj', 'xwdd', 'jd', 'wd', ]


"""*******************************教职工行为轨迹明细序列化*******************************"""


class XwgjJzgMxSerialiser(serializers.ModelSerializer):
    xwsj = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = wm.JzgXwgjGrgj
        fields = ['id', 'zgh', 'xwsj', 'xwdd', 'jd', 'wd', ]


"""*******************************研究生行为轨迹明细序列化*******************************"""


class XwgjYjsMxSerialiser(serializers.ModelSerializer):
    xwsj = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = wm.YjsXwgjGrgj
        fields = ['id', 'xh', 'xwsj', 'xwdd', 'jd', 'wd', ]
