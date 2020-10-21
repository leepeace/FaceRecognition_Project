# Generated by Django 3.1 on 2020-09-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_name', models.CharField(max_length=15)),
                ('company_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('company_phone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=30)),
                ('employee_phone', models.CharField(max_length=30)),
                ('employee_sex', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('PersonFace', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
