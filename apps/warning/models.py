# Create your models here.

from django.db import models

kqzt_CHOICES = (
    (0, '停用'),
    (1, '启用'),
)


# 系统管理之预警阈值设置
class XtglYjyzsz(models.Model):
    code = models.CharField("唯一标识", max_length=32, )
    yjmc = models.CharField('预警名称', max_length=32, )
    red = models.CharField("红色等级", max_length=32, null=True)
    orange = models.CharField("橙色等级", max_length=32, null=True)
    yellow = models.CharField("黄色等级", max_length=32, null=True)
    yjgz = models.CharField('预警规则', max_length=32)
    yjms = models.CharField('预警描述', max_length=512, null=True, )
    kqzt = models.IntegerField("开启状态", choices=kqzt_CHOICES, default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'xtgl_yjyzsz'
        verbose_name = "预警阈值设置"
        verbose_name_plural = verbose_name


# # 系统管理之预警阈值设置之晚归预警修改
#
#
# class XtglYjyzszWgyj(models.Model):
#     yjmc = models.CharField('预警名称', max_length=32, )
#     red = models.CharField("等级红时间段", max_length=32, )
#     orange = models.CharField("等级橙色时间段", max_length=32, )
#     yellow = models.CharField("等级黄色时间段", max_length=32, )
#     yjms = models.CharField('预警描述', max_length=512, null=True, )
#     kqzt = models.IntegerField("开启状态", default=0)
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)
#     update_time = models.DateTimeField('更新时间', auto_now=True)
#
#     class Meta:
#         db_table = 'yjyzsz_wg'
#         verbose_name = "预警阈值设置之晚归预警修改"
#         verbose_name_plural = verbose_name
#
#
# # 系统管理之预警阈值设置之在籍在校不选课预警修改
# class XtglYjyzszZjzxbxk(models.Model):
#     yjmc = models.CharField('预警名称', max_length=32, )
#     zjzxbxkjs = models.IntegerField('在籍在校不选课节数', default=0)
#     yjms = models.CharField('预警描述', max_length=512, null=True, )
#     kqzt = models.IntegerField("开启状态", default=0)
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)
#     update_time = models.DateTimeField('更新时间', auto_now=True)
#
#     # xtglyjsz = models.OneToOneField("XtglYjyzsz", on_delete=models.CASCADE, default=1)
#
#     class Meta:
#         db_table = 'yjyzsz_zjzxbxk'
#         verbose_name = "预警阈值设置之在籍在校不选课预警修改"
#         verbose_name_plural = verbose_name
#
#
# # 系统管理之预警阈值设置之逃课预警修改
# class XtglYjyzszTk(models.Model):
#     yjmc = models.CharField('逃课预警', max_length=32)
#     tks = models.IntegerField('逃课数', default=0)
#     yjms = models.CharField('预警描述', max_length=512, null=True, )
#     kqzt = models.IntegerField("开启状态", default=0)
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)
#     update_time = models.DateTimeField('更新时间', auto_now=True)
#
#     class Meta:
#         db_table = 'yjyzsz_tkxw'
#         verbose_name = "预警阈值设置之逃课预警修改"
#         verbose_name_plural = verbose_name
#
#
# # 系统管理之预警阈值设置之休学退学不离校预警修改
# class XtglYjyzszXxtxblx(models.Model):
#     yjmc = models.CharField('预警名称', max_length=32, )
#     red = models.IntegerField('红色等级天数', default=0)
#     orange = models.IntegerField('橙色等级天数', default=0)
#     yellow = models.IntegerField('黄色等级天数', default=0)
#     yjms = models.CharField('预警描述', max_length=512, null=True, )
#     kqzt = models.IntegerField("开启状态", default=0)
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)
#     update_time = models.DateTimeField('更新时间', auto_now=True)
#
#     class Meta:
#         db_table = 'yjyzsz_xxtxblx'
#         verbose_name = "预警阈值设置之休学退学不离校预警修改"
#         verbose_name_plural = verbose_name
#
#
# # 系统管理之预警阈值设置之校外住宿预警修改
# class XtglYjyzszXwzs(models.Model):
#     yjmc = models.CharField('预警名称', max_length=32, )
#     red = models.IntegerField('红色等级天数', default=0)
#     orange = models.IntegerField('橙色等级天数', default=0)
#     yellow = models.IntegerField('黄色等级天数', default=0)
#     yjms = models.CharField('预警描述', max_length=512, null=True, )
#     kqzt = models.IntegerField("开启状态", default=0)
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)
#     update_time = models.DateTimeField('更新时间', auto_now=True)
#
#     class Meta:
#         db_table = 'yjyzsz_xwzs'
#         verbose_name = "预警阈值设置之校外住宿预警修改"
#         verbose_name_plural = verbose_name
#
#
# # 系统管理之预警阈值设置之不在校预警修改
# class XtglYjyzszBzx(models.Model):
#     yjmc = models.CharField('预警名称', max_length=32, )
#     red = models.IntegerField('红色等级天数', default=0)
#     orange = models.IntegerField('橙色等级天数', default=0)
#     yellow = models.IntegerField('黄色等级天数', default=0)
#     yjms = models.CharField('预警描述', max_length=512)
#     kqzt = models.IntegerField("开启状态", default=0)
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)
#     update_time = models.DateTimeField('更新时间', auto_now=True)
#
#     class Meta:
#         db_table = 'yjyzsz_bzxyj'
#         verbose_name = "预警阈值设置之不在校预警修改"
#         verbose_name_plural = verbose_name
#

'''
***************************************智能预警*****************************************
'''

from apps.portrait.models import UibeBzks

Clzt_Choices = (
    (0, '未处理'),
    (1, '确认预警'),
    (2, '取消预警'),

)

Yjdj_Choices = (
    (0, '黄'),
    (1, '橙'),
    (2, '红'),

)


# 智能预警之在籍在校不选课预警
class ZnyjZjzxbxk(models.Model):
    xh = models.CharField(max_length=32)
    yjrq = models.DateField('预警日期', )
    sjxf = models.IntegerField("实际学分", default=0, null=True, )
    yxxf = models.IntegerField("应修学分", default=0, null=True, )
    wxkxq = models.CharField("未选课学期", max_length=32, null=True, )
    clzt = models.IntegerField(choices=Clzt_Choices, default=0)
    by1 = models.CharField("备用", max_length=32, null=True, )
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UibeBzks, related_name="zjzxbxk", on_delete=models.CASCADE)

    class Meta:
        db_table = 'znyj_zjzxbxk'
        verbose_name = "智能预警--在籍在校不选课预警"
        verbose_name_plural = verbose_name


# 智能预警之退学休学不离校预警
class ZnyjXxtxblx(models.Model):
    xh = models.CharField(max_length=32)
    yjrq = models.DateTimeField('预警日期', auto_now_add=True)
    txxx = models.DateField('退学休学日期', auto_now_add=True, null=True, )
    yjqk = models.CharField('预警情况', max_length=32, null=True, )
    yjdj = models.IntegerField(choices=Yjdj_Choices, default=0, null=True, )
    clzt = models.IntegerField(choices=Clzt_Choices, default=0)
    by1 = models.CharField("备用", max_length=32, null=True, )
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UibeBzks, related_name="xxtxblx", on_delete=models.CASCADE)

    class Meta:
        db_table = 'znyj_xxtxblx'
        verbose_name = "智能预警之休学退学不离校预警"
        verbose_name_plural = verbose_name


# 智能预警之校外住宿预警
class ZnyjXwzsyj(models.Model):
    # xh = models.ForeignKey('portrait.UibeBzks', max_length=32, on_delete=models.CASCADE, )
    xh = models.CharField(max_length=32)
    yjrq = models.DateTimeField('预警日期', auto_now_add=True)
    xwzsts = models.IntegerField('校外住宿天数', default=0, null=True)
    yjqk = models.CharField('预警情况', max_length=32, null=True)
    yjdj = models.IntegerField(choices=Yjdj_Choices, default=0)
    clzt = models.IntegerField(choices=Clzt_Choices, default=0)
    by1 = models.CharField('备用', max_length=32, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UibeBzks, related_name="xwzs", on_delete=models.CASCADE)

    class Meta:
        db_table = 'znyj_xwzs'
        verbose_name = "智能预警--校外住宿预警"
        verbose_name_plural = verbose_name


# 智能预警之不在校预警
class ZnyjBzx(models.Model):
    xh = models.CharField(max_length=32)
    yjrq = models.DateTimeField('预警日期', auto_now_add=True)
    bzxsj = models.CharField('不在校时间', max_length=32)
    bzxsc = models.IntegerField('不在校时长', default=0)
    yjdj = models.IntegerField(choices=Yjdj_Choices, default=0, )
    clzt = models.IntegerField(choices=Clzt_Choices, default=0, )
    by1 = models.CharField('备用', max_length=32, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UibeBzks, related_name="bzx", on_delete=models.CASCADE)

    class Meta:
        db_table = 'znyj_bzxyj'
        verbose_name = "智能预警之不在校预警"
        verbose_name_plural = verbose_name


# 智能预警之逃课行为预警

class ZnyjTkxw(models.Model):
    xh = models.CharField(max_length=32)
    yjrq = models.DateTimeField('预警日期', auto_now_add=True)
    kcsd = models.CharField('课程时段', max_length=32)
    kcmc = models.CharField('课程名称', max_length=64)
    yjqk = models.CharField('预警情况', max_length=64)
    yjdj = models.IntegerField(choices=Yjdj_Choices, default=0, )
    clzt = models.IntegerField(choices=Clzt_Choices, default=0, )
    by1 = models.CharField('备用', max_length=32, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UibeBzks, related_name="tkxw", on_delete=models.CASCADE)

    class Meta:
        db_table = 'znyj_tkxw'
        verbose_name = "智能预警之逃课行为预警"
        verbose_name_plural = verbose_name


# 智能预警之晚归预警
class ZnyjWgyj(models.Model):
    yjqk_Choices = (
        (1, '宿舍楼刷卡进入'),
        (2, '宿舍楼刷卡出'),
        (3, '网络连接'),
        (4, '宿舍楼以外区域刷E卡'),

    )
    xh = models.CharField(max_length=32)
    yjsj = models.DateTimeField('预警时间', null=True)
    wgsj = models.DateTimeField('晚归时间', null=True)
    yjqk = models.IntegerField('预警情况', choices=yjqk_Choices, default=0, )
    yjdj = models.IntegerField(choices=Yjdj_Choices, default=0, )
    clzt = models.IntegerField(choices=Clzt_Choices, default=0, )
    by1 = models.CharField('备用', max_length=32, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UibeBzks, related_name="wg", on_delete=models.CASCADE)

    class Meta:
        db_table = 'znyj_wg'
        verbose_name = "智能预警--晚归宿预警"
        verbose_name_plural = verbose_name


# 智能预警之上网行为预警
class ZnyjSwxw(models.Model):
    xh = models.CharField(max_length=32)
    syll = models.FloatField('使用流量', default=0.0, null=True, )
    by1 = models.CharField('备用', max_length=32, null=True)
    swsj = models.DateField('上网时间')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UibeBzks, related_name="swxw", on_delete=models.CASCADE)

    class Meta:
        db_table = 'znyj_swxw'
        verbose_name = "智能预警之上网行为"
        verbose_name_plural = verbose_name


# 行为轨迹之个人轨迹
class XwgjGrgj(models.Model):
    xh = models.CharField(max_length=32)
    # todo 新增 swsj,xwdd,jd,wd
    xwsj = models.DateTimeField('行为时间', null=True, )
    xwdd = models.CharField('行为地点', max_length=64, null=True, )
    jd = models.CharField('经度', max_length=64, null=True, )
    wd = models.CharField('纬度', max_length=64, null=True, )
    by1 = models.CharField('备用', max_length=32, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UibeBzks, related_name="grgj", on_delete=models.CASCADE)

    class Meta:
        db_table = 'xwgj_grgj'
        verbose_name = "行为轨迹个人轨迹"
        verbose_name_plural = verbose_name


# todo 新增 院系，年级，班级表
'''院系表'''


class Yx(models.Model):
    code = models.CharField('院系代码', max_length=16, null=True)
    name = models.CharField('院系名称', max_length=32, null=True)

    class Meta:
        db_table = 'bzks_yx'
        verbose_name = "院系表"
        verbose_name_plural = verbose_name


'''年级表'''


class Nj(models.Model):
    code = models.CharField('年级代码', max_length=16, null=True)
    name = models.CharField('年级名称', max_length=32, null=True)
    p_yx = models.ForeignKey(Yx, related_name='nj', on_delete=models.CASCADE, )

    class Meta:
        db_table = 'bzks_nj'
        verbose_name = "年级表"
        verbose_name_plural = verbose_name


'''班级表'''


class Bj(models.Model):
    code = models.CharField('班级代码', max_length=16, null=True)
    name = models.CharField('班级名称', max_length=16, null=True)
    p_nj = models.ForeignKey(Nj, related_name='bj', on_delete=models.CASCADE, )

    class Meta:
        db_table = 'bzks_bj'
        verbose_name = "班级表"
        verbose_name_plural = verbose_name


"""下拉列表"""


class Spinner(models.Model):
    yxbj = models.CharField(max_length=50, verbose_name='院系班级名称')
    pid = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='addinfo', null=True, blank=True,
                            verbose_name='上一级学院的id')

    # on_delete = models.CASCADE # 删除关联数据的时候，与之相关联的也删除
    # on_delete = models.DO_NOTHING # ... , 什么操作也不做
    # on_delete = models.PROTECT # ... ,引发报错
    # on_delete = models.SET_NULL # ... ,设置为空
    # on_delete = models.SET_DEFAULT # ... , 设置为默认值
    # on_delete = models.SET # ... , 删除关联数据
    class Meta:
        db_table = 'Spinner'

    def __str__(self):
        return self.yxbj
