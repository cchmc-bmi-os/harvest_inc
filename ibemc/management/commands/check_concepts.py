from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from avocado.models import DataCategory, DataConcept, DataField
import urllib2, json

# CONCEPT_SET = ['all', ]
BASE_URL = 'http://127.0.0.1:8005'

def check_py_concept(c):
    """Checks that a concept is defined by at least one field.

    """
    fields = DataField.objects.filter(concepts=c.id)
    if fields.count() > 0:
        pass ##print('Concept {} defined by {} -- OK'.format(c.id, ','.join([str(f.id) for f in fields])))
    else:
        raise Exception('Concept is not defined by any field.')

def check_api_concept(c):
    url = BASE_URL + '/api/concepts/' + str(c.id) + '/'
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    assert len(data) > 0, 'Error: concept json does not contain information'

def check_api_field(c):
    url = BASE_URL + '/api/fields/' + str(c.id) + '/'
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    assert len(data) > 0, 'Error: Field json does not contain information'


def check_concepts(concepts):
    to_delete = []
    for c in concepts:
        try:
            check_py_concept(c)
            check_api_concept(c)
            print('Concept {} - OK'.format(c.id))
        except Exception as E:
            print('Error in definition of concept id {}'.format(c.id))
            print(E)
            to_delete.append(c)
            print('Concept to be deleted')

    DataConcept.objects.filter(id__in=[c.id for c in to_delete]).delete()
    print('{} Concepts deleted'.format(len(to_delete)))


def check_fields(fields):
    to_delete = []
    for c in fields:
        try:
            check_api_field(c)
            print('Field {} - OK'.format(c.id))
        except Exception as E:
            print('Error in definition of field id {}'.format(c.id))
            print(E)
            ## to_delete.append(c)
            ## print('Field to be deleted')

    ## DataField.objects.filter(id__in=[c.id for c in to_delete]).delete()
    ## print('{} Fields deleted'.format(len(to_delete)))
    print('No field deleted - check code')


class Command(BaseCommand):
    """Check the definition of each concept.

    """
    help = 'Check the definition of the concepts defined in the database'

    option_list = BaseCommand.option_list + (
        make_option(
            '--concepts',
            dest='concepts',
            default='all',
            help='Load the specified set of concepts.',
        ),
    )

    def handle(self, *args, **options):
        print('Start...')
        # concepts = DataConcept.objects.all()
        # print('Number of concepts = {}'.format(concepts.count()))
        # check_concepts(concepts)

        fields = DataField.objects.all()
        print('Number of fileds = {}'.format(fields.count()))
        check_fields(fields)

        print('Done.')
