# Generated by Django 3.2 on 2021-10-31 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211030_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='short_description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
