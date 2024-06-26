# Generated by Django 5.0.4 on 2024-06-25 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_aadhar_employee_blood_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterEmployeeType',
            fields=[
                ('employee_type_id', models.CharField(max_length=2, unique=True)),
                ('employee_type', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_no',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.masteremployeetype'),
            preserve_default=False,
        ),
    ]
