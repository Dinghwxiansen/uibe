# Generated by Django 2.0 on 2020-01-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0066_uibejzg_zcxx'),
    ]

    operations = [
        migrations.CreateModel(
            name='JzgZcxq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zgh', models.CharField(max_length=16, verbose_name='职工号')),
                ('ZWPDRQ', models.CharField(max_length=16, verbose_name='职务变动日期')),
                ('ZYJSZWMC', models.CharField(max_length=16, verbose_name='专业技术职务名称')),
                ('ZYJSZWJB', models.CharField(max_length=16, verbose_name='专业技术职务级别')),
            ],
            options={
                'verbose_name': '教职工职称详情',
                'verbose_name_plural': '教职工职称详情',
                'db_table': 'jzg_Zcxq',
            },
        ),
    ]
