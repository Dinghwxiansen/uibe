# Generated by Django 2.0 on 2020-03-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20200305_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.IntegerField(choices=[(1, '启用'), (2, '停用')], default=1, verbose_name='状态'),
        ),
    ]
