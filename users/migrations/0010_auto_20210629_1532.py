# Generated by Django 3.2.3 on 2021-06-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210625_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='corranswer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='option_1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='option_2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='option_3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='option_4',
            field=models.TextField(),
        ),
    ]