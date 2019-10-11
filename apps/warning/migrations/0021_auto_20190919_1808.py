# Generated by Django 2.0 on 2019-09-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warning', '0020_auto_20190919_0933'),
    ]

    operations = [
        migrations.DeleteModel(
            name='XtglYjyzszBzx',
        ),
        migrations.DeleteModel(
            name='XtglYjyzszTk',
        ),
        migrations.DeleteModel(
            name='XtglYjyzszWgyj',
        ),
        migrations.DeleteModel(
            name='XtglYjyzszXwzs',
        ),
        migrations.DeleteModel(
            name='XtglYjyzszXxtxblx',
        ),
        migrations.DeleteModel(
            name='XtglYjyzszZjzxbxk',
        ),
        migrations.RemoveField(
            model_name='xtglyjyzsz',
            name='tks',
        ),
        migrations.AddField(
            model_name='xtglyjyzsz',
            name='yjgz',
            field=models.CharField(default=None, max_length=32, verbose_name='预警规则'),
        ),
        migrations.AlterField(
            model_name='xtglyjyzsz',
            name='kqzt',
            field=models.IntegerField(choices=[(0, '停用'), (1, '启用')], default=0, verbose_name='开启状态'),
        ),
    ]
