# Generated by Django 2.0 on 2019-09-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xtglyjyzszzjzxbxk',
            name='zjzxbxk',
            field=models.IntegerField(default=0, verbose_name='在籍在校不选课节数'),
        ),
    ]
