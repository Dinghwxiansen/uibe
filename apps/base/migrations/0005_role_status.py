# Generated by Django 2.0 on 2020-01-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200113_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='status',
            field=models.IntegerField(choices=[(1, '未拥有'), (2, '已拥有')], default=1, verbose_name='状态'),
        ),
    ]