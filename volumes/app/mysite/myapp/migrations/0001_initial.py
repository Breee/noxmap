# Generated by Django 2.0.2 on 2018-03-05 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('poke_nr', models.IntegerField(primary_key=True, serialize=False)),
                ('poke_name_ger', models.CharField(max_length=30)),
                ('poke_name_eng', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('poke_nr',),
            },
        ),
        migrations.CreateModel(
            name='PokePosition',
            fields=[
                ('poke_pos_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('poke_lvl', models.IntegerField(default=0, max_length=3)),
                ('poke_iv', models.IntegerField(default=0, max_length=3)),
                ('poke_lat', models.FloatField()),
                ('poke_lon', models.FloatField()),
                ('poke_visible', models.BooleanField(default=False)),
                ('poke_nr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Pokemon')),
            ],
        ),
    ]