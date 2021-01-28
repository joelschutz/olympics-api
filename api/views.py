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
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
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
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
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
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    filterset_fields = ('id', 'name')

class AthleteViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
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
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
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
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Competition.objects.select_related('sport')
    serializer_class = CompetitionSerializer
    filterset_fields = ('id', 'name', 'sport')

class MedalViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
    filterset_fields = ('id', 'name')
