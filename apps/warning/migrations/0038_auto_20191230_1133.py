# Generated by Django 2.0 on 2019-12-30 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warning', '0037_znyjzjzxbxk_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='znyjzjzxbxk',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zjzxbxk', to='portrait.UibeBzks'),
        ),
    ]
