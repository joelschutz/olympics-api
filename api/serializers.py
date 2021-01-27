from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Athlete, NOC, Game, Sport, Event, Competition, Medal

class AthleteSerializer(ModelSerializer):
    """
    This is a Serializer for the Athlete Model
    """
    class Meta:
        model = Athlete
        fields = [
            'id',
            'name',
            'sex',
            'height',
            'weight'
            ]

class NOCSerializer(ModelSerializer):
    """
    This is a Serializer for the NOC Model
    """
    class Meta:
        model = NOC
        fields = [
            'id',
            'noc',
            'region',
            'notes'
            ]

class GameSerializer(ModelSerializer):
    """
    This is a Serializer for the Game Model
    """
    class Meta:
        model = Game
        fields = [
            'id',
            'year',
            'season',
            'city'
            ]

class SportSerializer(ModelSerializer):
    """
    This is a Serializer for the Sport Model
    """
    class Meta:
        model = Sport
        fields = [
            'id',
            'name'
            ]

class CompetitionSerializer(ModelSerializer):
    """
    This is a Serializer for the Competition Model. It also implements custom create() and update() methods to interact with nested objects.
    """
    sport = SportSerializer(many=False)

    class Meta:
        model = Competition
        fields = [
            'id',
            'name',
            'sport'
            ]
    
    def create(self, validated_data):
        sport_data = validated_data.pop('sport')

        sport = Sport.objects.get_or_create(**sport_data)

        competition = Competition.objects.create(
            sport=sport,
            **validated_data
            )
        return competition

    def update(self, competition, validated_data):
        sport_data = validated_data.pop('sport')

        sport_serializer = SportSerializer(
            competition.sport,
            sport_data
        )
        if sport_serializer.is_valid(): 
            sport_serializer.save()
        else:
            ValidationError(sport_serializer.errors)
        
        competition.name = validated_data.get('name', competition.name)
        competition.save()

        return competition

class MedalSerializer(ModelSerializer):
    """
    This is a Serializer for the Medal Model
    """
    class Meta:
        model = Medal
        fields = [
            'id',
            'name'
            ]

class EventSerializer(ModelSerializer):
    """
    This is a Serializer for the Athlete Model. It also implements custom create() and update() methods to interact with nested objects.
    """
    athlete = AthleteSerializer(many=False)
    athlete_NOC = NOCSerializer(many=False)
    game = GameSerializer(many=False)
    competition = CompetitionSerializer(many=False)
    medal = MedalSerializer(many=False)
    
    class Meta:
        model = Event
        fields = [
            'id',
            'athlete',
            'athlete_age',
            'athlete_team',
            'athlete_NOC',
            'game',
            'competition',
            'medal'
            ]
    
    def create(self, validated_data):
        athlete_data = validated_data.pop('athlete')
        noc_data = validated_data.pop('athlete_NOC')
        game_data = validated_data.pop('game')
        competition_data = validated_data.pop('competition')
        sport_data = competition_data.pop('sport')
        medal_data = validated_data.pop('medal')


        athlete = Athlete.objects.get_or_create(**athlete_data)
        noc = NOC.objects.get_or_create(**noc_data)
        game = Game.objects.get_or_create(**game_data)
        sport = Sport.objects.get_or_create(**sport_data)
        competition = Competition.get_or_create(sport=sport, **competition_data)
        medal = Medal.objects.get_or_create(**medal_data)

        event = Event.objects.create(
            athlete=athlete,
            athlete_NOC=noc,
            game=game,
            competition=competition,
            medal=medal,
            **validated_data
            )

        return event
    
    def update(self, event, validated_data):

        athlete_data = validated_data.pop('athlete')
        noc_data = validated_data.pop('athlete_NOC')
        game_data = validated_data.pop('game')
        competition_data = validated_data.pop('competition')
        medal_data = validated_data.pop('medal')

        athlete_serializer = AthleteSerializer(
            event.athlete,
            athlete_data
        )
        if athlete_serializer.is_valid(): 
            athlete_serializer.save()
        else:
            ValidationError(athlete_serializer.errors)
        
        noc_serializer = NOCSerializer(
            event.athlete_NOC,
            noc_data
        )
        if noc_serializer.is_valid(): 
            noc_serializer.save()
        else:
            ValidationError(noc_serializer.errors)

        game_serializer = GameSerializer(
            event.game,
            game_data
        )
        if game_serializer.is_valid(): 
            game_serializer.save()
        else:
            ValidationError(game_serializer.errors)

        competition_serializer = CompetitionSerializer(
            event.competition,
            competition_data
        )
        if competition_serializer.is_valid(): 
            competition_serializer.save()
        else:
            ValidationError(competition_serializer.errors)
        
        medal_serializer = MedalSerializer(
            event.medal,
            medal_data
        )
        if medal_serializer.is_valid(): 
            medal_serializer.save()
        else:
            ValidationError(medal_serializer.errors)

        event.athlete_age = validated_data.get('athlete_age', event.athlete_age)
        event.athlete_team = validated_data.get('athlete_team', event.athlete_team)
        event.save()

        return event
