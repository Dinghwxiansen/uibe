# Generated by Django 2.0 on 2019-09-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0016_zcdj'),
    ]

    operations = [
        migrations.AddField(
            model_name='uibebzks',
            name='jg',
            field=models.IntegerField(choices=[(0, '默认'), (1, '北京')], default=0, verbose_name='籍贯'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='sfsqxwzs',
            field=models.IntegerField(choices=[(0, '未申请'), (1, '已申请')], default=0, verbose_name='是否申请校外住宿'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='sftx',
            field=models.IntegerField(choices=[(0, '默认'), (1, '退学')], default=0, verbose_name='退学状态'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='sfxx',
            field=models.IntegerField(choices=[(0, '默认'), (1, '休学')], default=0, verbose_name='休学状态'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='sfzx',
            field=models.IntegerField(choices=[(0, '在校'), (1, '不在校')], default=0, verbose_name='是否在校'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xjzt',
            field=models.IntegerField(choices=[(0, '在籍'), (1, '休学'), (2, '退学')], default=0, verbose_name='学籍状态'),
        ),
        migrations.AddField(
            model_name='uibebzks',
            name='xslb',
            field=models.IntegerField(choices=[(0, '默认'), (1, '交流生')], default=0, verbose_name='学生类别'),
        ),
        migrations.AlterField(
            model_name='uibebzks',
            name='sfyx',
            field=models.IntegerField(choices=[(0, '无效'), (1, '有效')], default=1, verbose_name='是否有效'),
        ),
    ]
