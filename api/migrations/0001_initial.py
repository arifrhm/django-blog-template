# Generated by Django 4.2.10 on 2024-03-11 04:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]