# Generated by Django 3.1.1 on 2020-10-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUpdates',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_title', models.CharField(max_length=200)),
                ('news_desc_1', models.TextField()),
                ('news_desc_2', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
