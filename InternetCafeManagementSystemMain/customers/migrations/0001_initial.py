# Generated by Django 5.1.2 on 2024-11-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('middleName', models.CharField(blank=True, max_length=255, null=True)),
                ('contactNumber', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
