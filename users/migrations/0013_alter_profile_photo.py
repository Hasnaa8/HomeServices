# Generated by Django 5.0.3 on 2024-05-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='default.jfif', upload_to='photos/%y/%m/%d'),
        ),
    ]
