# Generated by Django 3.2.24 on 2024-05-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0005_addobservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adddiagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=50)),
                ('diagnosiscode', models.CharField(max_length=50)),
            ],
        ),
    ]
