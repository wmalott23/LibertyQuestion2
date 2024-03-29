# Generated by Django 4.0.5 on 2022-06-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('birth_Date', models.DateField()),
                ('ethnicity', models.CharField(max_length=25)),
                ('work_address', models.CharField(max_length=255)),
                ('home_address', models.CharField(max_length=255)),
                ('additional_address', models.CharField(max_length=255)),
                ('work_phone', models.IntegerField(max_length=10)),
                ('home_phone', models.IntegerField(max_length=10)),
                ('additional_phone', models.IntegerField(max_length=10)),
            ],
        ),
    ]
