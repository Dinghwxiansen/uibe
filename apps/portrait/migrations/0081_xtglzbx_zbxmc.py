# Generated by Django 2.0 on 2020-09-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0080_remove_xtglzbx_zbxmc'),
    ]

    operations = [
        migrations.AddField(
            model_name='xtglzbx',
            name='zbxmc',
            field=models.CharField(default='abc', max_length=32, verbose_name='指标项名称'),
        ),
    ]