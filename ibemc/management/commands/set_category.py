from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from avocado.models import DataCategory, DataConcept, DataField

SUBJECT = ('Subject', {'published':True, 'order': 1})
DIAGNOSIS = ('Diagnosis', {'published':True, 'order': 2})
COMPLETE_CAT = ('Form', {'published':True, 'order': 700})
INTERNALS = ('Internals', {'published':True, 'order': 800})
UNUSED = ('Unused', {'published':False, 'order': 900})
CATEGORY_DEFAULT = {'published':True, 'order':100}

FIELD2CAT = {
    'Ibem-Is Id': INTERNALS,
    'Redcap Event Name': INTERNALS,
    'Ibemc Center Name': INTERNALS,
    'Event Type': UNUSED,
    'Number Of Valid Visits': UNUSED,
    }

MODEL2CAT = {
    'subject': SUBJECT,
    'intakedemographic': ('Intake Demographics', CATEGORY_DEFAULT)
}

def set_category(concept):
    field = concept.fields.all()[0]
    cat = None

    ## Specific cases
    if concept.name in FIELD2CAT:
        cat_name = FIELD2CAT[concept.name][0]
        cat_default = FIELD2CAT[concept.name][1]
        cat, created = DataCategory.objects.get_or_create(
            name=cat_name,
            defaults=cat_default
        )
        concept.category = cat
        concept.save()
        return cat

    ## agw
    if 'age' in concept.name.lower():
        cat_name = SUBJECT[0]
        cat_default = SUBJECT[1]
        cat, created = DataCategory.objects.get_or_create(
            name=cat_name,
            defaults=cat_default
        )
        concept.category = cat
        concept.save()
        return cat


    ## Diagnosis
    if 'diagnosis' in concept.name.lower() or 'condition' in concept.name.lower():
        cat_name = DIAGNOSIS[0]
        cat_default = DIAGNOSIS[1]
        cat, created = DataCategory.objects.get_or_create(
            name=cat_name,
            defaults=cat_default
        )
        concept.category = cat
        concept.save()
        return cat


    ## Specific classes
    if concept.name.endswith(' Complete'):
        cat_name = COMPLETE_CAT[0]
        cat_default = COMPLETE_CAT[1]
        cat, created = DataCategory.objects.get_or_create(
            name=cat_name,
            defaults=cat_default
        )
        concept.category = cat
        concept.save()
        return cat

    print('field.model_name', field.model_name)
    m = [ k for k in MODEL2CAT if k in field.model_name]
    assert len(m) <= 1, 'Multiple category found for concept {}'.format(concept.name)


    ## Maps form to category
    if len(m) == 1 :
        form = m[0]
        cat_name = MODEL2CAT[form][0]
        cat_default = MODEL2CAT[form][1]
        cat, created = DataCategory.objects.get_or_create(
            name=cat_name,
            defaults=cat_default
        )
        concept.category = cat
        concept.save()
        return cat

    ## No category found
    print('No category found for concept {}'.format(concept.name))

    return(None)

class Command(BaseCommand):
    """Impute category to concept

    """
    help = 'Impute category to categories'

    # option_list = BaseCommand.option_list + (
    #     make_option(
    #         '--override',
    #         dest='override',
    #         default=False,
    #         help='Overrides existing category.',
    #     ),
    # )

    def handle(self, *args, **options):
        print('Start...')
        for concept in DataConcept.objects.all():
            cat = set_category(concept)
            print('Category {} to Category {}'.format(cat.name if cat else 'UNMODIFIED', concept.name))

        print('Done.')
