# Generated by Django 2.2.2 on 2019-07-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0012_auto_20190713_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='last_donated_date',
            field=models.CharField(max_length=30),
        ),
    ]
