# Generated by Django 4.2.6 on 2024-01-10 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact_computers_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Man',
            new_name='Man_clothes',
        ),
        migrations.RenameModel(
            old_name='Womans',
            new_name='Womans_clothes',
        ),
    ]
