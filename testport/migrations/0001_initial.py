# Generated by Django 5.1.6 on 2025-03-13 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=40)),
                ('Project_name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('Project_photo', models.ImageField(upload_to='images')),
                ('live_site_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='testport.project')),
            ],
        ),
    ]
