# Generated by Django 2.0 on 2019-12-26 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0050_auto_20191226_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dw',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portrait.UibeBzks'),
        ),
    ]