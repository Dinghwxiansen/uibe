# Generated by Django 2.0 on 2019-09-05 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0007_sjzb_sjzbzd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sjzbzd',
            name='sjzb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sjzbzd', to='portrait.Sjzb'),
        ),
    ]
