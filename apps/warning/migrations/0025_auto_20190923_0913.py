# Generated by Django 2.0 on 2019-09-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warning', '0024_znyjswxw_swsj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='znyjswxw',
            name='swsj',
            field=models.DateField(verbose_name='上网时间'),
        ),
    ]
