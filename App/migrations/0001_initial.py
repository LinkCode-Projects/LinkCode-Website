# Generated by Django 3.1.1 on 2020-10-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('tech_id', models.AutoField(primary_key=True, serialize=False)),
                ('tech_name', models.CharField(max_length=30)),
                ('tech_desc', models.CharField(max_length=60)),
            ],
        ),
    ]