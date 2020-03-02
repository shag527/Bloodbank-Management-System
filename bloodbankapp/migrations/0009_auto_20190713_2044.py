# Generated by Django 2.2.2 on 2019-07-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0008_auto_20190713_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brequests',
            name='status',
            field=models.IntegerField(choices=[(0, 'pending'), (1, 'approve'), (2, 'done')]),
        ),
        migrations.AlterField(
            model_name='donors',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
    ]