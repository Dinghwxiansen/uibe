# Generated by Django 2.0 on 2020-06-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0073_auto_20200416_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uibebzks',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='uibejzg',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]