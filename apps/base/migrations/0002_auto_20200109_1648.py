# Generated by Django 2.0 on 2020-01-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='head',
            field=models.ImageField(null=True, upload_to='photos', verbose_name='头像'),
        ),
    ]
