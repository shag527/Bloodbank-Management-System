# Generated by Django 2.2.2 on 2019-07-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('address', models.TextField(max_length=300)),
                ('contact_number', models.CharField(max_length=15)),
                ('blood_group', models.CharField(max_length=4)),
                ('last_donated_date', models.DateField()),
                ('major_illness', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('the_link', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('attendant_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('blood_group', models.CharField(max_length=4)),
                ('quantity', models.IntegerField()),
                ('hospital_name', models.CharField(max_length=100)),
                ('deadline', models.DateField()),
            ],
        ),
    ]