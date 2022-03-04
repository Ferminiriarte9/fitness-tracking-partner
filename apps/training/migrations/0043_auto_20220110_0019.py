# Generated by Django 3.2 on 2022-01-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0042_remove_exercise_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='status',
        ),
        migrations.AddField(
            model_name='routine',
            name='tags',
            field=models.ManyToManyField(blank=True, to='training.Tag'),
        ),
    ]