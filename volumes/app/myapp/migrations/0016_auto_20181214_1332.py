# Generated by Django 2.1.3 on 2018-12-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alloweddiscordserver'),
    ]

    operations = [
        migrations.AddField(
            model_name='alloweddiscordserver',
            name='server_id',
            field=models.CharField(db_index=True, default=None, max_length=128),
            preserve_default=False,
        ),
    ]
