# Generated by Django 2.0.2 on 2019-04-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='location',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]