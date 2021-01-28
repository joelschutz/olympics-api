from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import (
    Event,
    NOC,
    Sport,
    Game,
    Athlete,
    Competition,
    Medal
    )
from .serializers import (
    EventSerializer,
    NOCSerializer,
    SportSerializer,
    GameSerializer,
    AthleteSerializer,
    CompetitionSerializer,
    MedalSerializer
    )
from .filters import EventFilter

class EventViewSet(ModelViewSet):
    """
    This is a ViewSet for the Event Model. See /events in https://github.com/joelschutz/olympics-api/blob/master/README.md for more info.
    """

    queryset = Event.objects.select_related(
        'athlete',
        'athlete_NOC',
        'game',
        'competition',
        'medal'
    )
    serializer_class = EventSerializer
    filterset_class = EventFilter

class NOCViewSet(ModelViewSet):
    """
    This is a ViewSet for the NOC Model. See /nocs in https://github.com/joelschutz/olympics-api/blob/master/README.md for more info.
    """

    queryset = NOC.objects.all()
    serializer_class = NOCSerializer
    filterset_fields = (
        'id',
        'noc',
        'region',
        'notes'
        )

class SportViewSet(ModelViewSet):
    """
    This is a ViewSet for the Sport Model. See /sports in https://github.com/joelschutz/olympics-api/blob/master/README.md for more info.
    """

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    filterset_fields = ('id', 'name')

class AthleteViewSet(ModelViewSet):
    """
    This is a ViewSet for the Athlete Model. See /athletes in https://github.com/joelschutz/olympics-api/blob/master/README.md for more info.
    """

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filterset_fields = ('id',
        'name',
        'sex',
        'height',
        'weight'
        )

class GameViewSet(ModelViewSet):
    """
    This is a ViewSet for the Game Model. See /games in https://github.com/joelschutz/olympics-api/blob/master/README.md for more info.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filterset_fields = ('id',
        'year',
        'season',
        'city'
        )

class CompetitionViewSet(ModelViewSet):
    """
    This is a ViewSet for the Competition Model. See /competitions in https://github.com/joelschutz/olympics-api/blob/master/README.md for more info.
    """

    queryset = Competition.objects.select_related('sport')
    serializer_class = CompetitionSerializer
    filterset_fields = ('id', 'name', 'sport')

class MedalViewSet(ModelViewSet):
    """
    This is a ViewSet for the Medal Model. See /medals in https://github.com/joelschutz/olympics-api/blob/master/README.md for more info.
    """

    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
    filterset_fields = ('id', 'name')
