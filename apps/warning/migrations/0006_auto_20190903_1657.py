# Generated by Django 2.0 on 2019-09-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warning', '0005_auto_20190903_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xtglyjyzszbzx',
            name='by1',
        ),
        migrations.RemoveField(
            model_name='xtglyjyzszbzx',
            name='by2',
        ),
        migrations.RemoveField(
            model_name='xtglyjyzszxwzs',
            name='by1',
        ),
        migrations.RemoveField(
            model_name='xtglyjyzszxwzs',
            name='by2',
        ),
        migrations.AddField(
            model_name='xtglyjyzszbzx',
            name='kqzt',
            field=models.IntegerField(default=0, verbose_name='开启状态'),
        ),
        migrations.AddField(
            model_name='xtglyjyzsztk',
            name='kqzt',
            field=models.IntegerField(default=0, verbose_name='开启状态'),
        ),
        migrations.AddField(
            model_name='xtglyjyzszwgyj',
            name='kqzt',
            field=models.IntegerField(default=0, verbose_name='开启状态'),
        ),
        migrations.AddField(
            model_name='xtglyjyzszxwzs',
            name='kqzt',
            field=models.IntegerField(default=0, verbose_name='开启状态'),
        ),
        migrations.AddField(
            model_name='xtglyjyzszxxtxblx',
            name='kqzt',
            field=models.IntegerField(default=0, verbose_name='开启状态'),
        ),
        migrations.AddField(
            model_name='xtglyjyzszzjzxbxk',
            name='kqzt',
            field=models.IntegerField(default=0, verbose_name='开启状态'),
        ),
    ]
