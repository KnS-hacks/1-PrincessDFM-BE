# Generated by Django 3.2.9 on 2021-11-17 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
