# Generated by Django 2.0 on 2020-01-09 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200109_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='head',
            field=models.CharField(max_length=32, null=True, verbose_name='头像'),
        ),
    ]
