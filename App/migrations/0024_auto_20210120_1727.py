# Generated by Django 3.1.1 on 2021-01-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(),
        ),
    ]