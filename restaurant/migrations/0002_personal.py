# Generated by Django 4.2.5 on 2023-09-25 17:54

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='İşçinin adı və soyadı')),
                ('position', models.CharField(max_length=255, verbose_name='İşçinin vəzifəsi')),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.upload_photo_for_personal, verbose_name='İşçinin fotosu')),
            ],
            options={
                'verbose_name': 'İşçi',
                'verbose_name_plural': 'İşçilər',
                'ordering': ('-created_at',),
            },
        ),
    ]
