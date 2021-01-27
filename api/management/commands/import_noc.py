from django.core.management.base import BaseCommand, CommandError
from api.models import NOC
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
                    noc, region, notes = row
                    if noc == 'NOC': continue

                    if noc == 'SIN': noc = 'SGP' # Correcting spelling bug in the dataset 

                    obj, created= NOC.objects.get_or_create(
                        noc=noc,
                        region=region,
                        notes=notes
                        )
                    if created: 
                    print(f'{obj} saved!')	                        obj.save()
                        print(f'{obj} saved!')
                    else:
                        print(f'{obj} already saved!')
        except FileNotFoundError as e:
            raise CommandError(e)
        
        