# Generated by Django 2.0 on 2019-11-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0037_auto_20191113_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='JzgBm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmdm', models.CharField(max_length=16, verbose_name='部门代码')),
                ('bm', models.CharField(max_length=32, verbose_name='部门')),
            ],
            options={
                'verbose_name': '教职工院系分类',
                'verbose_name_plural': '教职工院系分类',
                'db_table': 'jzg_Bm',
            },
        ),
        migrations.AddField(
            model_name='uibejzg',
            name='bmdm',
            field=models.CharField(max_length=32, null=True, verbose_name='部门代码'),
        ),
    ]