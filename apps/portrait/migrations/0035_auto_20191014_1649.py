# Generated by Django 2.0 on 2019-10-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0034_auto_20190927_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xtglzbx',
            name='jsgz',
            field=models.CharField(max_length=128, null=True, verbose_name='计算规则'),
        ),
        migrations.AlterField(
            model_name='xtglzbx',
            name='zdxz',
            field=models.CharField(max_length=128, null=True, verbose_name='字段选择'),
        ),
    ]