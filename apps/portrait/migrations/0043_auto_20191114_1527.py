# Generated by Django 2.0 on 2019-11-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0042_jzgbm_bmjc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jzgbm',
            name='bmjc',
            field=models.CharField(max_length=32, verbose_name='部门简称'),
        ),
    ]
