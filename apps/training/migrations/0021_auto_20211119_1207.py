# Generated by Django 3.2 on 2021-11-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0020_exercise_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exerciseroutine',
            old_name='minutes',
            new_name='duration',
        ),
        migrations.AddField(
            model_name='exerciseroutine',
            name='rest',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]