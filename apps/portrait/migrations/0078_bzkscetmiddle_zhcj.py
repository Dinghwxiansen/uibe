# Generated by Django 2.0 on 2020-08-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0077_auto_20200803_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='bzkscetmiddle',
            name='zhcj',
            field=models.IntegerField(default=0, null=True, verbose_name='综合成绩'),
        ),
    ]
