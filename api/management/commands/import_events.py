from django.core.management.base import BaseCommand, CommandError
from api.models import Athlete, NOC, Game, Sport, Event, Competition, Medal
from csv import reader

class Command(BaseCommand):
    help = 'Import Events from .csv file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='The .csv filename containing the NOC information')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        events = Event.objects.select_related(
        'athlete',
        'athlete_NOC',
        'game',
        'competition',
        'medal'
    )
        event_list = list(events.values_list('id', flat=True))
        athletes = Athlete.objects.all()
        games = Game.objects.all()
        sports = Sport.objects.all()
        competitions = Competition.objects.select_related('sport')
        medals= Medal.objects.all()
        nocs = NOC.objects.all()
        try:
            with open(filename) as file:
                r = reader(file)
                for n, row in enumerate(r):
                    pk, name, sex, age, height, weight, team, noc, game, year, season, city, sport, competition, medal = row
                    if pk == 'ID': continue
                    if event_list and (n == event_list[0]): 
                        print(f'Event {n} already saved!')
                        event_list.pop(0)
                        continue
                    athlete, created = athletes.get_or_create(
                        pk=pk,
                        name=name,
                        sex=sex,
                        height=round(float(height), 1) if height != 'NA' else None,
                        weight=round(float(weight), 1) if weight != 'NA' else None
                        )
                    if created: athlete.save()

                    noc = nocs.get(noc=noc)

                    game, created = games.get_or_create(
                        year=year,
                        season=season,
                        city=city
                        )
                    if created: game.save()

                    sport, created = sports.get_or_create(name=sport)
                    if created: sport.save()

                    competition, created = competitions.get_or_create(
                        name=competition,
                        sport=sport
                        )
                    if created: competition.save()

                    medal, created = medals.get_or_create(name=medal)
                    if created: medal.save()
                    
                    event, created = events.get_or_create(
                        athlete=athlete,
                        athlete_age=age if age != 'NA' else None,
                        athlete_team=team,
                        athlete_NOC=noc,
                        game=game,
                        competition=competition,
                        medal=medal
                    )
                    if created: 
                        event.save()
                        print(f'Event {n} saved!')
                    else:
                        print(f'Event {n} already saved!')
        except FileNotFoundError as e:
            raise CommandError(e)
        
        