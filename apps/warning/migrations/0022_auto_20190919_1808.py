# Generated by Django 2.0 on 2019-09-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warning', '0021_auto_20190919_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xtglyjyzsz',
            name='yjgz',
            field=models.CharField(max_length=32, verbose_name='预警规则'),
        ),
    ]
