# Generated by Django 3.2.9 on 2021-11-17 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MBTI',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=10)),
                ('introduce', models.CharField(blank=True, max_length=1000, null=True)),
                ('motto', models.CharField(blank=True, max_length=1000, null=True)),
                ('team', models.IntegerField(null=True)),
                ('github', models.URLField(blank=True, max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, max_length=100, null=True)),
                ('hashtag', models.ManyToManyField(blank=True, to='introduce.HashTag')),
                ('interest', models.ManyToManyField(blank=True, to='introduce.Interest')),
                ('mbti', models.ManyToManyField(blank=True, to='introduce.MBTI')),
                ('participate', models.ManyToManyField(blank=True, to='introduce.Participate')),
            ],
            options={
                'ordering': ['team'],
            },
        ),
    ]
