# Generated by Django 2.0 on 2019-11-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0041_auto_20191114_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='jzgbm',
            name='bmjc',
            field=models.CharField(max_length=32, null=True, verbose_name='部门简称'),
        ),
    ]