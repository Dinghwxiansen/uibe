# Generated by Django 2.0 on 2019-12-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0061_auto_20191230_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uibebzks',
            name='bh',
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='bj',
            field=models.CharField(max_length=32, null=True, verbose_name='班级名称'),
        ),
    ]
