# Generated by Django 2.1.3 on 2018-12-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20181211_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='quest_item_amount',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='quest_item_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='quest_pokemon_id',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='quest_reward_type',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='target',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
    ]
