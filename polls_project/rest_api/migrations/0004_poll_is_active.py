# Generated by Django 3.1.7 on 2021-03-31 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_auto_20210330_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Статус'),
        ),
    ]
