# Generated by Django 2.0 on 2019-09-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0013_xshxbq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xshxbq',
            name='xh',
            field=models.CharField(max_length=32, verbose_name='学号'),
        ),
    ]
