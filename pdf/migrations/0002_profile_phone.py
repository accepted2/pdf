# Generated by Django 5.1.2 on 2024-10-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
