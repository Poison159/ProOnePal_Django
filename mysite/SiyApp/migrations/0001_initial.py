# Generated by Django 2.1.4 on 2019-02-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeTeam', models.CharField(max_length=128)),
                ('awayTeam', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('pitch', models.CharField(max_length=128)),
                ('stage', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('age', models.IntegerField()),
                ('imgPath', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeGoals', models.IntegerField()),
                ('awayGaols', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('kasi', models.CharField(max_length=64)),
                ('imgPath', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('maxStages', models.IntegerField()),
                ('maxGames', models.IntegerField()),
                ('maxTeams', models.IntegerField()),
            ],
        ),
    ]
