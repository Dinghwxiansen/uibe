# Generated by Django 2.0 on 2019-12-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0048_auto_20191226_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uibebzks',
            name='zydm',
            field=models.CharField(max_length=64, null=True, verbose_name='专业代码'),
        ),
    ]