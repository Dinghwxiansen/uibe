# Generated by Django 2.0 on 2019-11-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0035_auto_20191014_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uibejzg',
            old_name='bkkcshjc',
            new_name='bkkcskjc',
        ),
        migrations.RenameField(
            model_name='uibejzg',
            old_name='cxxmsl',
            new_name='zxxmsl',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='by1',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='by2',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='ccxx',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='pthzs',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='rych',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='tsjy',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='wlsh',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='xznj',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='yx',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='yyzs',
        ),
        migrations.RemoveField(
            model_name='uibejzg',
            name='zcjbbdrq',
        ),
        migrations.AddField(
            model_name='uibejzg',
            name='jszgz',
            field=models.CharField(max_length=128, null=True, verbose_name='教师资格证'),
        ),
        migrations.AddField(
            model_name='uibejzg',
            name='tsjycs',
            field=models.IntegerField(default=0, null=True, verbose_name='图书借阅次数'),
        ),
        migrations.AddField(
            model_name='uibejzg',
            name='wlsyll',
            field=models.CharField(max_length=64, null=True, verbose_name='网络使用流量'),
        ),
        migrations.AddField(
            model_name='uibejzg',
            name='wlsysc',
            field=models.CharField(max_length=64, null=True, verbose_name='网络使用时长'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='create_time',
            field=models.DateField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='csrq',
            field=models.CharField(max_length=32, null=True, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='gqpxzs',
            field=models.CharField(max_length=128, null=True, verbose_name='岗前培训证书'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='jl',
            field=models.CharField(max_length=512, null=True, verbose_name='奖励'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='jsjzs',
            field=models.CharField(max_length=128, null=True, verbose_name='计算机证书'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='lxrq',
            field=models.CharField(max_length=64, null=True, verbose_name='来校日期'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='rylb',
            field=models.CharField(max_length=64, null=True, verbose_name='人员类别'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='update_time',
            field=models.DateField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='xl',
            field=models.CharField(max_length=64, null=True, verbose_name='学历'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='xm',
            field=models.CharField(max_length=128, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='xngw',
            field=models.CharField(max_length=256, null=True, verbose_name='校内岗位'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='xw',
            field=models.CharField(max_length=64, null=True, verbose_name='学位'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='yjfx',
            field=models.CharField(max_length=64, null=True, verbose_name='研究方向'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='zcjb',
            field=models.CharField(max_length=512, null=True, verbose_name='职称级别'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='zxsf',
            field=models.CharField(max_length=512, null=True, verbose_name='在校身份'),
        ),
    ]
