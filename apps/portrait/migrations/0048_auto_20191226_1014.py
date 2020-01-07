# Generated by Django 2.0 on 2019-12-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0047_auto_20191225_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uibebzks',
            old_name='fdy',
            new_name='fdyh',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='bj',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='jg',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='kssj',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='sftx',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='sfxx',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='sfyx',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='sfzx',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='tlcj',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='xb',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='xf',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='xzcj',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='ydcj',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='yx',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='zfcj',
        ),
        migrations.RemoveField(
            model_name='uibebzks',
            name='zsmc',
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='bh',
            field=models.CharField(max_length=32, null=True, verbose_name='班号'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='gjpyptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='国际培养平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='jdpercentile',
            field=models.CharField(max_length=32, null=True, verbose_name='绩点占百分比'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='jdpm',
            field=models.IntegerField(default=0, null=True, verbose_name='绩点排名'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='jdzf',
            field=models.CharField(max_length=32, null=True, verbose_name='绩点增幅'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='jycyptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='就业创业平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='jyczptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='箐英成长平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='sjyrptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='实践育人平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='sthdptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='社团活动平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='sxqjd',
            field=models.CharField(max_length=32, null=True, verbose_name='上学期绩点'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='sxydptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='思想引导平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='syd',
            field=models.CharField(max_length=32, null=True, verbose_name='生源地'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='tkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='逃课次数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='tsjyptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='通识教育平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xfpercentile',
            field=models.CharField(max_length=32, null=True, verbose_name='学分占百分比'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xkzxf',
            field=models.IntegerField(default=0, null=True, verbose_name='选课总学分'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xkzxfpercentile',
            field=models.CharField(max_length=32, null=True, verbose_name='选课总学分占百分比'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xkzxfpm',
            field=models.IntegerField(default=0, null=True, verbose_name='选课总学分排名'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xn',
            field=models.CharField(max_length=32, null=True, verbose_name='学年'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xq',
            field=models.CharField(max_length=16, null=True, verbose_name='学期'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xskyptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='学术科研平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xywhptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='校园文化平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='ydrq',
            field=models.CharField(max_length=32, null=True, verbose_name='异动日期'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='yxdm',
            field=models.CharField(max_length=16, null=True, verbose_name='院系代码'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='yxxf',
            field=models.CharField(max_length=32, null=True, verbose_name='已修学分'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='zydm',
            field=models.CharField(max_length=16, null=True, verbose_name='专业代码'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='zyfwptxkcs',
            field=models.IntegerField(default=0, null=True, verbose_name='志愿服务平台课程数'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='zyzxf',
            field=models.CharField(max_length=32, null=True, verbose_name='专业总学分'),
        ),
        migrations.AlterField(
            model_name='uibebzks',
            name='jd',
            field=models.CharField(max_length=32, null=True, verbose_name='绩点'),
        ),
        migrations.AlterField(
            model_name='uibebzks',
            name='xjzt',
            field=models.CharField(max_length=32, null=True, verbose_name='学籍状态'),
        ),
        migrations.AlterField(
            model_name='uibebzks',
            name='xznj',
            field=models.CharField(max_length=64, null=True, verbose_name='现在年级'),
        ),
    ]