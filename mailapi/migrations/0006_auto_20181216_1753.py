# Generated by Django 2.1.4 on 2018-12-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mailapi', '0005_auto_20181216_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='von',
            field=models.EmailField(max_length=254),
        ),
    ]
