# Generated by Django 2.0 on 2020-01-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warning', '0039_auto_20191230_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='znyjtkxw',
            name='yjsj',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='预警时间'),
        ),
    ]
