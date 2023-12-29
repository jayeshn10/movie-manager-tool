# Generated by Django 5.0 on 2023-12-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('action', 'Action'), ('drama', 'Drama'), ('comedy', 'Comedy'), ('sifi', 'Si-Fi'), ('adventure', 'Adventure'), ('horror', 'Horror'), ('romance', 'Romance'), ('family', 'Family'), ('animation', 'Animation'), ('documentary', 'Documentary')], max_length=20)),
                ('director', models.CharField(max_length=255)),
                ('producer', models.CharField(max_length=255)),
                ('writer', models.CharField(max_length=255)),
                ('rating', models.CharField(choices=[('g', 'G'), ('pg', 'PG'), ('pg-13', 'PG-13'), ('r', 'R'), ('nc-17', 'NC-17'), ('unrated', 'Unrated')], max_length=20)),
            ],
        ),
    ]
