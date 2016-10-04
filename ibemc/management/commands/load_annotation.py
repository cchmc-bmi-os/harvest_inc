from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from avocado.models import DataCategory, DataConcept, DataField
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


def load_annotation(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = '\t')
        for row in reader:
            try:
                field_name = row['field_label']
                ep = float(row['EP'])
                ea =float(row['EA'])
                if (ep + ea ) > 0:
                    prct_prov = round(100*(ep / (ep + ea)), 1)
                    prct_miss = 100 - prct_prov
                    prct_prov_str = str(prct_prov)
                    prct_miss_str = str(prct_miss)
                else:
                    prct_prov_str = 'NA'
                    prct_miss_str = 'NA'

                annotation = 'Data completness: (Provided | Missing | % Provided | % Missing) = ({} | {} | {}% | {}%)'.format(row['EP'], row['EA'], prct_prov_str, prct_miss_str)
                annotate_datafield(field_name, annotation)
            except Exception as Ex:
                print('Error while building annotation for {}'.format(field_name))
                print(Ex)


class Command(BaseCommand):
    """Annotate concept based on external file

    """
    help = 'Annotate data concept'

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
        load_annotation(filename)
        print('Done.')
