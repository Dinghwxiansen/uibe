# Generated by Django 2.0 on 2019-12-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warning', '0031_remove_znyjzjzxbxk_by1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='znyjwgyj',
            name='by1',
        ),
        migrations.AlterField(
            model_name='znyjbzx',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='znyjswxw',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='znyjtkxw',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='znyjwgyj',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='znyjwgyj',
            name='yjqk',
            field=models.CharField(max_length=64, verbose_name='预警情况'),
        ),
        migrations.AlterField(
            model_name='znyjxwzsyj',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='znyjxxtxblx',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='znyjzjzxbxk',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
    ]
