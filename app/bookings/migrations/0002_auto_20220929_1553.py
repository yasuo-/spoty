# Generated by Django 3.2.15 on 2022-09-29 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingcheckin',
            name='checkin',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='入店時間'),
        ),
        migrations.AlterField(
            model_name='bookingcheckout',
            name='checkout',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='当日のチェックアウト'),
        ),
    ]
