# Generated by Django 5.1.2 on 2024-10-29 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_alter_profile_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='previose_work',
            new_name='previous_work',
        ),
    ]
