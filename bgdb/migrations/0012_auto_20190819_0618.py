# Generated by Django 2.2.4 on 2019-08-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgdb', '0011_auto_20190819_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='average_weight',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
