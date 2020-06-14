from django.db import models

kqzt_CHOICES = (
    (0, '停用'),
    (1, '启用'),
)

SEX_CHOICES = (
    (0, '未知'),
    (1, '男'),
    (2, '女'),
)
Sfyx_Choices = (
    (0, '无效'),
    (1, '有效'),

)
BQQX_CHOICES = (
    (0, '全部'),
    (1, '学生'),
    (2, '教师'),)


# Create your models here.
# 数据表查询
class Sjzb(models.Model):
    zwbm = models.CharField('中文表名', max_length=32)
    ywbm = models.CharField('英文表名', max_length=32)

    class Meta:
        db_table = 'xtgl_sjzb'
        verbose_name = "系统管理之数据总表"
        verbose_name_plural = verbose_name


class Sjzbzd(models.Model):
    # todo  新增字段表名
    # bm = models.CharField('表名', max_length=32, )
    zwzdmc = models.CharField('中文字段名', max_length=32)
    zdsjbbs = models.CharField('字段数据表标识', max_length=32)
    sjlx = models.CharField('数据类型', max_length=32)
    ywbm = models.CharField('英文表名', max_length=32)
    bz = models.CharField('备注', max_length=32, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    sjzb = models.ForeignKey("Sjzb", on_delete=models.CASCADE, related_name="sjzbzd")

    class Meta:
        db_table = 'xtgl_sjzbzd'
        verbose_name = "系统管理之数据总表字段"
        verbose_name_plural = verbose_name


# 系统管理之标签维度表
class XtglBqwd(models.Model):
    wdmc = models.CharField('维度名称', max_length=32, null=False)
    wdms = models.CharField("维度描述", max_length=512, null=True)
    kqzt = models.IntegerField("开启状态", choices=kqzt_CHOICES, default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'xtgl_bqwd'
        verbose_name = "系统管理之标签维度设置"
        verbose_name_plural = verbose_name


# 系统管理之指标项管理
class XtglZbx(models.Model):
    ZBFL_CHOICES = (
        (0, '单字段指标项'),
        (1, '多字段指标项'),
    )
    zbxmc = models.CharField('指标项名称', max_length=32, null=False)
    zbfl = models.IntegerField('指标分类', choices=ZBFL_CHOICES, default=0)
    zbwd = models.CharField('指标维度', max_length=64, null=True)
    zdxz = models.CharField('字段选择', max_length=128, null=True)
    jsgz = models.CharField('计算规则', max_length=128, null=True)
    zbms = models.CharField('指标描述', max_length=512, null=True)
    kqzt = models.IntegerField("开启状态", choices=kqzt_CHOICES, default=0)
    sjzb_id = models.CharField('总表id', max_length=32)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'xtgl_zbx'
        verbose_name = "系统管理之指标项设置"
        verbose_name_plural = verbose_name


# 假期设置
class XtglJq(models.Model):
    jqmc = models.CharField('假期名称', max_length=32, null=False)
    jqkssj = models.DateField('假期开始时间')
    jqjssj = models.DateField('假期结束时间')
    jqms = models.CharField('假期描述', max_length=512, null=True)
    kqzt = models.IntegerField('假期状态', choices=kqzt_CHOICES, default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'xtgl_jq'
        verbose_name = "系统管理之假期设置"
        verbose_name_plural = verbose_name


# 系统管理之画像标签设置
class XtglBqsz(models.Model):
    Bqsz_CHOICES = (
        (0, '权重标签'),
        (1, '非权重标签'),
    )

    bqmc = models.CharField('标签名称', max_length=32, null=False)
    zbfl = models.IntegerField('指标分类', choices=Bqsz_CHOICES, default=0)
    zbwd = models.CharField('指标维度', max_length=32, null=False)
    zbx = models.CharField('指标项', max_length=32, null=False)
    bqgz = models.CharField('标签规则', max_length=512, null=False)
    bqSQL = models.CharField('标签规则SQL', max_length=512, null=True)
    bqms = models.CharField('标签描述', max_length=512, null=True)
    bqqx = models.IntegerField('标签权限', choices=BQQX_CHOICES, default=0)
    kqzt = models.IntegerField('标签开启状态', choices=kqzt_CHOICES, default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'xtgl_bqsz'
        verbose_name = "系统管理之画像标签设置"
        verbose_name_plural = verbose_name


# 教职工表
class UibeJzg(models.Model):

    id = models.CharField('id', max_length=32, null=False, primary_key=True)
    zgh = models.CharField('职工号', max_length=32, )
    xm = models.CharField('姓名', max_length=128, )
    xb = models.IntegerField(choices=SEX_CHOICES, default=0)
    csrq = models.CharField('出生日期', max_length=32, null=True)
    xw = models.CharField('学位', max_length=64, null=True)
    xl = models.CharField('学历', max_length=64, null=True)
    lxrq = models.CharField('来校日期', max_length=64, null=True)
    # yx = models.CharField('院系', max_length=64, null=True)
    # xznj = models.CharField('现在年级', max_length=64, null=True)# 去除
    zzmm = models.CharField('政治面貌', max_length=64, null=True)
    # yyzs = models.CharField("英语证书", max_length=32, null=True, ) # 去除
    jsjzs = models.CharField('计算机证书', max_length=128, null=True, )
    jszgz = models.CharField('教师资格证', max_length=128, null=True)
    gqpxzs = models.CharField('岗前培训证书', max_length=128, null=True, )
    # pthzs = models.CharField('普通话证书', max_length=32, null=True, ) # 去除
    qtzs = models.CharField('其他证书', max_length=64, null=True, )
    yjfx = models.CharField('研究方向', max_length=64, null=True, )
    zxxmsl = models.IntegerField('纵向项目数量', default=0, null=True, )
    hxxmsl = models.IntegerField('横向项目数量', default=0, null=True, )
    cgjlsl = models.IntegerField('成果奖励数量', default=0, null=True, )
    yjbgsl = models.IntegerField('研究报告数量', default=0, null=True, )
    zzcgsl = models.IntegerField('著作成果数量', default=0, null=True, )
    lwcgsl = models.IntegerField('论文成果数量', default=0, null=True, )
    bmdm = models.CharField('部门代码', max_length=32, null=True)
    bm = models.CharField('部门', max_length=64, null=True, )
    rylb = models.CharField('人员类别', max_length=64, null=True, )
    gwzj = models.CharField('岗位职级', max_length=64, null=True, )
    # zcxx = models.ForeignKey("DW", on_delete=models.DO_NOTHING,to_field="id")
    zcxxdm = models.CharField('职称信息代码', max_length=32, null=True)
    zcxx = models.CharField('职称信息', max_length=256, null=True)
    zcbdrq = models.CharField('职称变动日期', max_length=32, null=True)
    # zcxx = models.CharField('职称信息', max_length=256, null=True)
    # zcjb = models.CharField('职称级别', max_length=512, null=True, )
    # zcjbbdrq = models.DateField('职称级别变动日期', null=True)
    xngw = models.CharField('校内岗位', max_length=256, null=True, )
    zxsf = models.CharField('在校身份', max_length=512, null=True, )
    jl = models.CharField('奖励', max_length=512, null=True)
    yjskcxsrc = models.IntegerField('研究生课程学生人次', default=0, null=True, )
    yjskcskjc = models.IntegerField('研究生课程授课节次', default=0, null=True, )
    yjskcxss = models.IntegerField('研究生课程学时数', default=0, null=True, )
    yjskcskms = models.IntegerField('研究生课程授课门数', default=0, null=True, )
    bkkcxsrc = models.IntegerField('本科课程学生人数', default=0, null=True, )
    bkkcskjc = models.IntegerField('本科课程授课节次', default=0, null=True, )
    bkkcxss = models.IntegerField('本科课程学时数', default=0, null=True, )
    bkkcskms = models.IntegerField('本科课程授课门数', default=0, null=True, )
    tsjycs = models.IntegerField('图书借阅次数', default=0, null=True)
    ekxf = models.CharField('e卡消费', max_length=64, null=True, )
    wlsyll = models.CharField('网络使用流量', max_length=64, null=True)
    wlsysc = models.CharField('网络使用时长', max_length=64, null=True)
    create_time = models.DateField('创建时间', auto_now_add=True)
    update_time = models.DateField('更新时间', auto_now=True)

    class Meta:
        db_table = 'jzg'
        verbose_name = "教职工信息表"
        verbose_name_plural = verbose_name


class XshxBq(models.Model):
    BQQX_CHOICES = (
        (0, '全部'),
        (1, '学生'),
        (2, '教师'),)

    xh = models.CharField('学号', max_length=32)
    bq = models.CharField('标签', max_length=32, )
    bqsm = models.CharField('标签说明', max_length=32, null=True)
    bqqx = models.IntegerField('标签权限', choices=BQQX_CHOICES, default=0)
    sfyx = models.IntegerField('是否有效', choices=Sfyx_Choices, default=1)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'bzks_xshxbq'
        verbose_name = "用户画像之学生标签权限"
        verbose_name_plural = verbose_name


# 本专科生表
class UibeBzks(models.Model):
    id = models.CharField('id', max_length=32, null=False, primary_key=True)
    # 学号设置为主键
    # xh = models.CharField('学号', max_length=32, null=False, primary_key=True)
    XJZT_CHOICES = (
        (0, '在籍'),
        (1, '休学'),
        (2, '退学'),
    )
    JG_CHOICES = (
        (0, '默认'),
        (1, '北京'),
    )
    xh = models.CharField('学号', max_length=32, unique=True)
    xm = models.CharField('姓名', max_length=16, )
    xb = models.IntegerField(choices=SEX_CHOICES, default=0)
    syd = models.CharField('生源地', max_length=32, null=True)
    xznj = models.CharField('现在年级', max_length=64, null=True)
    xn = models.CharField('学年', max_length=32, null=True)
    xq = models.CharField('学期', max_length=16, null=True)
    fdy = models.CharField('辅导员', max_length=16, null=True)
    bj = models.CharField('班级名称', max_length=32, null=True)
    xjzt = models.CharField('学籍状态', max_length=32, null=True)
    ydrq = models.CharField('异动日期', max_length=32, null=True)
    yx = models.CharField('院系', max_length=16, null=True)
    # yxdm = models.ForeignKey("DW", on_delete=models.DO_NOTHING,to_field="id")
    zydm = models.CharField('专业代码', max_length=64, null=True)
    tkcs = models.IntegerField('逃课次数', default=0, null=True)
    jd = models.CharField('绩点', max_length=32, null=True)
    sxqjd = models.CharField('上学期绩点', max_length=32, null=True)
    jdpm = models.IntegerField('绩点排名', default=0, null=True)
    jdzf = models.CharField('绩点增幅', max_length=32, null=True)
    jdpercentile = models.CharField('绩点占百分比', max_length=32, null=True)
    xkzxf = models.IntegerField('选课总学分', default=0, null=True)
    xkzxfpm = models.IntegerField('选课总学分排名', default=0, null=True)
    xkzxfpercentile = models.CharField('选课总学分占百分比', max_length=32, null=True)
    sxydptxkcs = models.IntegerField('思想引导平台课程数', null=True, default=0)
    tsjyptxkcs = models.IntegerField('通识教育平台课程数', null=True, default=0)
    gjpyptxkcs = models.IntegerField('国际培养平台课程数', null=True, default=0)
    xywhptxkcs = models.IntegerField('校园文化平台课程数', null=True, default=0)
    sthdptxkcs = models.IntegerField('社团活动平台课程数', null=True, default=0)
    sjyrptxkcs = models.IntegerField('实践育人平台课程数', null=True, default=0)
    xskyptxkcs = models.IntegerField('学术科研平台课程数', null=True, default=0)
    zyfwptxkcs = models.IntegerField('志愿服务平台课程数', null=True, default=0)
    jycyptxkcs = models.IntegerField('就业创业平台课程数', null=True, default=0)
    jyczptxkcs = models.IntegerField('箐英成长平台课程数', null=True, default=0)
    xfpercentile = models.CharField('学分占百分比', max_length=32, null=True)
    yxxf = models.CharField('已修学分', max_length=32, null=True)
    zyzxf = models.CharField('专业总学分', max_length=32, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'bzks'
        verbose_name = "本专科生信息表"
        verbose_name_plural = verbose_name


# 研究生表

class UibeYjs(models.Model):
    id = models.CharField('id', max_length=32, null=False, primary_key=True)
    xh = models.CharField('学号', max_length=32, unique=True)
    xm = models.CharField('姓名', max_length=16, )
    xb = models.IntegerField(choices=SEX_CHOICES, default=0)
    yx = models.CharField('院系', max_length=64, null=True)
    xn = models.CharField('学年', max_length=32, null=True)
    zy = models.CharField('专业', max_length=64, null=True)
    dszgh = models.CharField('导师职工号', max_length=16, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'yjs'
        verbose_name = "研究生信息表"
        verbose_name_plural = verbose_name


class Zcdj(models.Model):
    code = models.CharField('职工号', max_length=32)
    zcjb = models.CharField('职称级别', max_length=32)

    class Meta:
        db_table = 'jzg_zcdj'
        verbose_name = "职称等级"
        verbose_name_plural = verbose_name


class JzgZcxx(models.Model):
    zwdm = models.CharField('职务代码', max_length=16)
    zwmc = models.CharField('职务名称', max_length=32)
    zwjb = models.CharField('职务级别', max_length=32, null=True)

    class Meta:
        db_table = 'jzg_Zc'
        verbose_name = "教职工职务分类"
        verbose_name_plural = verbose_name


class JzgZcxq(models.Model):
    zgh = models.CharField('职工号', max_length=16)
    ZWPDRQ = models.CharField('职务变动日期', max_length=16, null=True)
    ZYJSZWMC = models.CharField('专业技术职务名称', max_length=16, null=True)
    ZYJSZWJB = models.CharField('专业技术职务级别', max_length=16, null=True)

    class Meta:
        db_table = 'jzg_Zcxq'
        verbose_name = "教职工职称详情"
        verbose_name_plural = verbose_name


# todo 测试自定义规则表
class BzksMiddle(models.Model):
    xsh = models.CharField('学生号', max_length=128)
    qkcs = models.IntegerField('翘课次数')
    cjpm = models.IntegerField('成绩排名')
    jdsf = models.IntegerField('绩点上浮')


# 单位
class DW(models.Model):
    id = models.IntegerField('院系代码', null=False, primary_key=True)
    yxmc = models.CharField('院系名称', max_length=32)


#  todo:本专科生四六级非权重标签 数据处理中间表
class BzksCETMiddle(models.Model):
    xh = models.CharField('学号', max_length=32, unique=True)
    kssj = models.CharField('考试时间', max_length=64)
    tlcj = models.IntegerField("听力成绩", null=True, default=0)
    ydcj = models.IntegerField("阅读成绩", null=True, default=0)
    xzcj = models.IntegerField("写作成绩", null=True, default=0)
    zfcj = models.IntegerField("总分成绩", null=True, default=0)
    zfpm = models.IntegerField("总分排名", null=True, default=0)
    zfpercentile = models.CharField("总分排名百分比", max_length=32)
    zsmc = models.CharField("总分名称", max_length=32)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'bzks_cet'
        verbose_name = "本专科四六级数据处理中间表"
        verbose_name_plural = verbose_name


# todo:本专科生图书借阅数据处理中间表
class BzksTSJYMiddle(models.Model):
    xh = models.CharField('学号', max_length=32, unique=True)
    xb = models.IntegerField(choices=SEX_CHOICES, default=0)
    zcs = models.IntegerField("总册数", default=0, null=True)
    zcspm = models.IntegerField("总册数排名", null=True, default=0)
    zcspetcentile = models.CharField("总册数排名百分比", max_length=64)
    highlb = models.CharField("借阅最高册数类别", max_length=32)
    highcs = models.IntegerField("借阅最高类别册数", null=True, default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'bzks_tsjy'
        verbose_name = "本专科图书借阅数据处理中间表"
        verbose_name_plural = verbose_name


# todo:本专科生E卡消费数据处理中间表
class BzksEKMiddle(models.Model):
    xh = models.CharField('学号', max_length=32, unique=True)
    txamt = models.CharField('消费总金额', max_length=32, null=True)
    txamtpm = models.IntegerField('消费总金额排名', null=True)
    txamtpetcentile = models.CharField('消费总金额排名百分比', max_length=32, null=True)
    ztcs = models.IntegerField('当月澡堂次数', null=True, default=0)
    stskcs = models.IntegerField('当月食堂刷卡次数', null=True, default=0)
    stskcspm = models.IntegerField('当月食堂刷卡次数排名', null=True, default=0)
    stskcspetcentile = models.CharField('当月食堂刷卡次数排名百分比', max_length=32, null=True)
    zccs = models.IntegerField('当月早餐消费次数', null=True, default=0)
    wccs = models.IntegerField('当月午餐消费次数', null=True, default=0)
    wcxfcs = models.IntegerField('当月晚餐消费次数', null=True, default=0)
    ystjyje = models.CharField('当月一食堂交易金额', null=True, max_length=32)
    ystjyjepm = models.IntegerField('一食堂交易金额排名', null=True, default=0)
    ystjyjepercent = models.CharField('一食堂交易金额排名所占百分比', max_length=32, null=True)
    estjyje = models.CharField('当月二食堂交易金额', null=True, max_length=32)
    estjyjepm = models.IntegerField('二食堂交易金额排名', null=True, default=0)
    estjyjepercent = models.CharField('二食堂交易金额排名所占百分比', max_length=32, null=True)
    sstjyje = models.CharField('当月三食堂交易金额', null=True, max_length=32)
    sstjyjepm = models.IntegerField('三食堂交易金额排名', null=True, default=0)
    sstjyjepercent = models.CharField('三食堂交易金额排名所占百分比', max_length=32, null=True)
    qzstjyje = models.CharField('当月清真食堂交易金额', null=True, max_length=32)
    qzstjyjepm = models.IntegerField('清真食堂交易金额排名', null=True, default=0)
    qzstjyjepercent = models.CharField('清真食堂交易金额排名所占百分比', max_length=32, null=True)
    hywmjyje = models.CharField('当月虹远物美白月光交易金额', null=True, max_length=32)
    hywmjyjepm = models.IntegerField('虹远物美白月光交易金额排名', null=True, default=0)
    hywmjyjepercent = models.CharField('虹远物美白月光交易金额排名所占百分比', max_length=32, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'bzks_ek'
        verbose_name = "本专科E卡消费数据处理中间表"
        verbose_name_plural = verbose_name
