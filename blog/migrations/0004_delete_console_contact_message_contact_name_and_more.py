# Generated by Django 4.2.6 on 2024-01-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_man_man_clothes_rename_womans_womans_clothes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Console',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
