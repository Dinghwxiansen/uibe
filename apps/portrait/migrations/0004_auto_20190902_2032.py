# Generated by Django 2.0 on 2019-09-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0003_auto_20190902_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xtgljq',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='xtgljq',
            name='jqjssj',
            field=models.DateField(verbose_name='假期结束时间'),
        ),
        migrations.AlterField(
            model_name='xtgljq',
            name='jqkssj',
            field=models.DateField(verbose_name='假期开始时间'),
        ),
        migrations.AlterField(
            model_name='xtgljq',
            name='jqms',
            field=models.CharField(max_length=512, null=True, verbose_name='假期描述'),
        ),
        migrations.AlterField(
            model_name='xtgljq',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
