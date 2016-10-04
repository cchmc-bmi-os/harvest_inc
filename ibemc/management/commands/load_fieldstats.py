from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from hub.models import Fieldstats
import csv


def annotate_datafield(field_name, annotation):
    '''Presently working with a limited subset of redcap fields.
    Most fields won't be found.

    '''
    try:
        c = DataField.objects.filter(name__iexact = field_name)[0]
        c.description = annotation
        c.save()
        print('--> Annotated field {}'.format(field_name))
    except Exception as E:
        pass
        ## print('Error while annotating {}: {}'.format(field_name, E))


def load_stats(filename, dataset = u'IBEMC'):
    Fieldstats.objects.all().delete();
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = '\t')
        for row in reader:
            try:
                field_name = row['field_name']
                field_label = row['field_label']
                ep = int(row['EP']) if row['EP'] else None
                ea =int(row['EA']) if row['EA'] else None
                np =int(row['NP']) if row['NP'] else None
                na =int(row['NA']) if row['NA'] else None
                fa =int(row['FA']) if row['FA'] else None

                fs = Fieldstats()
                fs.dataset = dataset
                fs.field_name = field_name
                fs.field_label = field_label
                fs.ep = ep
                fs.ea = ea
                fs.np = np
                fs.na = na
                fs.fa = fa

                fs.save()

            except Exception as Ex:
                print('Error while loading field stats for {}'.format(field_name))
                print(Ex)


class Command(BaseCommand):
    """Load field stats into hub database

    """
    help = 'Load field stats into hub database'

    option_list = BaseCommand.option_list + (
        make_option(
            '--stats_file',
            dest='stats_file',
            help='File containing stats on fields.',
        ),
    )

    def handle(self, *args, **options):
        print('Start...')
        filename = options['stats_file']
        load_stats(filename)
        print('Done.')
