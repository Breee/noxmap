# Generated by Django 2.1.4 on 2018-12-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20181211_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointofinterest',
            name='last_modified',
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='last_modified',
            field=models.BigIntegerField(default=None, null=True),
        ),
    ]
