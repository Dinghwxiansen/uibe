# Generated by Django 2.0 on 2019-09-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0030_auto_20190924_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xtglbqsz',
            name='zbfl',
            field=models.IntegerField(choices=[(0, '权重标签'), (1, '非权重标签')], default=0, verbose_name='指标分类'),
        ),
    ]
