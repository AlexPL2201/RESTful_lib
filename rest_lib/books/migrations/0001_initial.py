# Generated by Django 5.1.5 on 2025-01-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publication_year', models.DateField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
