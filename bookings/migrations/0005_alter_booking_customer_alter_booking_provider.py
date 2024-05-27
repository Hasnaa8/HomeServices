# Generated by Django 5.0.6 on 2024-05-27 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_customer_alter_booking_provider_and_more'),
        ('users', '0027_remove_profile_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_booking', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_booking', to='users.profile'),
        ),
    ]
