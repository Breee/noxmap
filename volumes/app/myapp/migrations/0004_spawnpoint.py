# Generated by Django 2.1.4 on 2018-12-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181203_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpawnPoint',
            fields=[
                ('id', models.BigIntegerField(max_length=15, primary_key=True, serialize=False)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
    ]