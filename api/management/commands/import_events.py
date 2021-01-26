from django.core.management.base import BaseCommand, CommandError
from api.models import Athlete, NOC, Game, Sport, Event, Competition, Medal
from csv import reader

class Command(BaseCommand):
    help = 'Import NOCs from .csv file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='The .csv filename containing the NOC information')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        try:
            with open(filename) as file:
                r = reader(file)
                for row in r:
                    pk, name, sex, age, height, weight, team, noc, game, year, season, city, sport, competition, medal = row
                    if pk == 'ID': continue

                    athlete, created = Athlete.objects.get_or_create(
                        pk=pk,
                        name=name,
                        sex=sex,
                        height=round(float(height), 1) if height != 'NA' else None,
                        weight=round(float(weight), 1) if weight != 'NA' else None
                        )
                    if created: athlete.save()

                    noc = NOC.objects.get(noc=noc)

                    game, created = Game.objects.get_or_create(
                        year=year,
                        season=season,
                        city=city
                        )
                    if created: game.save()

                    sport, created = Sport.objects.get_or_create(name=sport)
                    if created: sport.save()

                    competition, created = Competition.objects.get_or_create(
                        name=competition,
                        sport=sport
                        )
                    if created: competition.save()

                    medal, created = Medal.objects.get_or_create(name=medal)
                    if created: medal.save()
                    
                    event, created = Event.objects.get_or_create(
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
                        print(f'{event} saved!')
                    else:
                        print(f'{event} already saved!')
        except FileNotFoundError as e:
            raise CommandError(e)
        
        