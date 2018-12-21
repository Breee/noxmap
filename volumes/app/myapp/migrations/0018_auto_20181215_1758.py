# Generated by Django 2.1.3 on 2018-12-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20181214_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raid',
            old_name='pokemon',
            new_name='pokemon_id',
        ),
        migrations.RemoveField(
            model_name='raid',
            name='end',
        ),
        migrations.RemoveField(
            model_name='raid',
            name='spawn',
        ),
        migrations.RemoveField(
            model_name='raid',
            name='start',
        ),
        migrations.AddField(
            model_name='raid',
            name='move_1',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='raid',
            name='move_2',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='raid',
            name='poi_id',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='raid',
            name='pokemon_form',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='raid',
            name='time_battle',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='raid',
            name='time_end',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='raid',
            name='time_start',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='raid',
            name='cp',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='raid',
            name='moves',
            field=models.ManyToManyField(blank=True, default=None, to='myapp.PokemonMove'),
        ),
    ]