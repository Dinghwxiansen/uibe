# Generated by Django 2.0 on 2020-01-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0065_delete_jzgbm'),
    ]

    operations = [
        migrations.AddField(
            model_name='uibejzg',
            name='zcxx',
            field=models.CharField(max_length=256, null=True, verbose_name='职称信息'),
        ),
    ]
