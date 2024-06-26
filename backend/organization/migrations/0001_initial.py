# Generated by Django 5.0.6 on 2024-06-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=350)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(max_length=6)),
                ('phone_no', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('gst_no', models.CharField(max_length=15)),
            ],
        ),
    ]
