# Generated by Django 3.2.3 on 2021-06-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=3)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]
