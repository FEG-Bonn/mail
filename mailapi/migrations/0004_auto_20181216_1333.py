# Generated by Django 2.1.4 on 2018-12-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mailapi', '0003_auto_20181216_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='objekt',
            field=models.CharField(blank=True, default='Kein Object.', max_length=120),
        ),
    ]
