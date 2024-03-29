from django.contrib import admin

from django.contrib import admin
from .models import League, Team, Player, Match, Event

class EventInline(admin.TabularInline):
    model = Event
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super(EventInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'player':
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(team__in=[request._obj_.home_team, request._obj_.away_team])
            else:
                field.queryset = field.queryset.none()
        return field

class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'league', 'date')
    inlines = [EventInline]

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super(MatchAdmin, self).get_form(request, obj, **kwargs)

class EventAdmin(admin.ModelAdmin):
    list_display = ('match', 'type', 'player', 'time')

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match, MatchAdmin)
admin.site.register(Event, EventAdmin)