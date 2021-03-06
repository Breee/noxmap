from django.contrib import admin
from myapp.models import PointOfInterest, Pokemon, PokemonSpawn, PokemonType, SpawnPoint, Quest, \
    Mapper, \
    AllowedDiscordServer, Raid

from rest_framework.authtoken.admin import TokenAdmin


class PointOfInterestAdmin(admin.ModelAdmin):
    search_fields = ['type', 'name', 'poi_id', 'last_modified']


class QuestAdmin(admin.ModelAdmin):
    search_fields = ['quest_id', 'pokestop_id', 'quest_pokemon_id', 'quest_item_id', 'quest_reward_type']


class RaidAdmin(admin.ModelAdmin):
    search_fields = ['poi_id', 'gym__name', 'pokemon_id__name_german', 'pokemon_id', 'level']


# Register your models here.
admin.site.register(Pokemon)
admin.site.register(PokemonSpawn)
admin.site.register(SpawnPoint)
admin.site.register(PokemonType)
admin.site.register(Quest, QuestAdmin)
admin.site.register(AllowedDiscordServer)
admin.site.register(Mapper)
admin.site.register(PointOfInterest, PointOfInterestAdmin)
admin.site.register(Raid, RaidAdmin)


TokenAdmin.raw_id_fields = ('user',)
