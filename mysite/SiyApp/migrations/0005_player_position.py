# Generated by Django 2.1.4 on 2019-02-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiyApp', '0004_auto_20190221_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default='GK', max_length=128),
        ),
    ]