# Generated by Django 5.0.4 on 2024-06-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='aadhar',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='blood_group',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='leaving_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='leaving_reason',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='pan',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
