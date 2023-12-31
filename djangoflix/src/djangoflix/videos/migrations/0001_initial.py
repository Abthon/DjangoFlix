# Generated by Django 4.2.4 on 2023-08-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True)),
                ('video_id', models.CharField(max_length=300)),
            ],
        ),
    ]
