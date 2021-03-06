# Generated by Django 3.2.3 on 2021-06-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_chat_reg_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=10)),
                ('marks', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('option_3', models.CharField(max_length=100)),
                ('option_4', models.CharField(max_length=100)),
                ('corranswer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuizBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=10)),
            ],
        ),
    ]
