# Generated by Django 2.0 on 2019-09-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0012_auto_20190910_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='XshxBq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xh', models.CharField(max_length=32, unique=True, verbose_name='学号')),
                ('bq', models.CharField(max_length=32, verbose_name='标签')),
                ('bqsm', models.CharField(max_length=32, null=True, verbose_name='标签说明')),
                ('bqqx', models.IntegerField(choices=[(0, '全部'), (1, '学生'), (2, '教师')], default=0, verbose_name='标签权限')),
                ('create_user', models.CharField(max_length=32, null=True, verbose_name='创建者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户画像之学生标签权限',
                'verbose_name_plural': '用户画像之学生标签权限',
                'db_table': 'xshxbq',
            },
        ),
    ]
