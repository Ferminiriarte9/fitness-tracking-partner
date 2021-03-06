# Generated by Django 3.2 on 2021-10-30 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_delete_routineevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='routine',
        ),
        migrations.AddField(
            model_name='routine',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='EventExcercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=30)),
                ('cycles', models.IntegerField(blank=True, null=True)),
                ('repetitions', models.IntegerField(blank=True, null=True)),
                ('minutes', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.event')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.exercise')),
            ],
        ),
    ]
