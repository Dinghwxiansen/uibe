# Generated by Django 2.0 on 2019-09-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0011_auto_20190909_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='xtglbqsz',
            name='kqzt',
            field=models.IntegerField(default=0, verbose_name='标签开启状态'),
        ),
        migrations.AlterField(
            model_name='xtglbqsz',
            name='bqms',
            field=models.CharField(max_length=512, null=True, verbose_name='标签描述'),
        ),
        migrations.AlterField(
            model_name='xtglbqsz',
            name='zbfl',
            field=models.IntegerField(choices=[(1, '权重标签'), (2, '非权重标签')], default=1, verbose_name='指标分类'),
        ),
    ]
