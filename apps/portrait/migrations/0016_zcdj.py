# Generated by Django 2.0 on 2019-09-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0015_uibejzg_zcjbbdrq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zcdj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, verbose_name='职工号')),
                ('zcjb', models.CharField(max_length=32, verbose_name='职称级别')),
            ],
            options={
                'verbose_name': '职称等级',
                'verbose_name_plural': '职称等级',
                'db_table': 'zcdj',
            },
        ),
    ]
