# Generated by Django 2.0 on 2020-04-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200305_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.IntegerField(choices=[(0, '启用'), (1, '停用')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.IntegerField(choices=[(0, '启用'), (1, '停用')], default=1, verbose_name='状态'),
        ),
    ]
