# Generated by Django 2.1.4 on 2018-12-19 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mailapi', '0006_auto_20181216_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
