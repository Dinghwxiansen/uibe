# Generated by Django 2.0 on 2019-09-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0019_auto_20190919_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xtglbqsz',
            name='kqzt',
            field=models.IntegerField(choices=[(0, '停用'), (1, '启用')], default=0, verbose_name='标签开启状态'),
        ),
        migrations.AlterField(
            model_name='xtglbqwd',
            name='kqzt',
            field=models.IntegerField(choices=[(0, '停用'), (1, '启用')], default=0, verbose_name='开启状态'),
        ),
        migrations.AlterField(
            model_name='xtgljq',
            name='kqzt',
            field=models.IntegerField(choices=[(0, '停用'), (1, '启用')], default=0, verbose_name='假期状态'),
        ),
    ]
