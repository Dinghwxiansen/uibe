# Generated by Django 2.0 on 2020-01-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0067_jzgzcxq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jzgzcxq',
            name='ZWPDRQ',
            field=models.CharField(max_length=16, null=True, verbose_name='职务变动日期'),
        ),
        migrations.AlterField(
            model_name='jzgzcxq',
            name='ZYJSZWJB',
            field=models.CharField(max_length=16, null=True, verbose_name='专业技术职务级别'),
        ),
        migrations.AlterField(
            model_name='jzgzcxq',
            name='ZYJSZWMC',
            field=models.CharField(max_length=16, null=True, verbose_name='专业技术职务名称'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xb',
            field=models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0),
        ),
    ]
