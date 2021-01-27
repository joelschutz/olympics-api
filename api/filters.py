from django_filters.rest_framework import FilterSet, NumberFilter, CharFilter
from .models import Event

class EventFilter(FilterSet):
    """
    This custom FilterSet implements logic for filtering Events, in addition of the default fields, by sport, season and year.
    """
    sport = NumberFilter('competition__sport__id')
    season = CharFilter('game__season')
    year = NumberFilter('game__year')
    class Meta:
        model = Event
        fields = ['id',
        'athlete',
        'athlete_age',
        'athlete_team',
        'athlete_NOC',
        'game',
        'sport',
        'competition',
        'year',
        'season',
        'medal']
