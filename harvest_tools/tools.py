## cat ibemc/etl/3-RevisedConcepts20170426/update_concepts_20170426.py | grep -v '"""' | bin/manage.py shell

from avocado.models import DataCategory, DataField, DataConceptField, DataConcept

## Utils
##############################
def raise_exception(message):
    raise Exception(message)

def print_log(message):
    print(message)

def update_attributes(objs, params, log):
    for obj in objs:
        for p in params:
            param = params[p]

            if p =='parent_category':
                p = 'parent'
                parent = DataCategory.objects.filter(name=param)
                if len(parent) == 0:
                    log('parent_category {0} not found for {1}'.format(param, obj))
                    param = None
                else:
                    param = parent[0]

            if p == 'category_name':
                p = 'category'
                category = DataCategory.objects.filter(name=param)
                if len(category) == 0:
                    log('Category {0} not found for {1}'.format(param, obj))
                    param = None
                else:
                    param = category[0]

            if p == 'fields_name':
                ## p won't be an attr of obj. Fields are added below
                ## since it is not possible to add many to many
                ## records when the though table has been explicitely
                ## defined.
                fields = []
                for fname in param:
                    f = DataField.objects.filter(name=fname)
                    if len(f) == 0:
                        log('datafield {0} not found for {1}'.format(f, obj))
                        f = None
                    else:
                        f = f[0]
                    if f:
                        fields.append(f)

                DataConceptField.objects.filter(concept=obj).delete()
                for f in fields:
                    dc = DataConceptField()
                    dc.concept = obj
                    dc.field = f
                    dc.save()

                param = fields

            if hasattr(obj, p):
                setattr(obj, p, param)
            elif p!='fields_name':
                log('Object {0} has no attribute {1}'.format(obj, p))

        obj.save()

def update_object(object_key, object_type, params, stop_on_error=False, create_if_not_exists=False, key='name'):
    if stop_on_error:
        log = raise_exception
    else:
        log = print_log

    # Tries to first modify published concepts
    if object_type == DataConcept:
        filters = {key: object_key, 'published': True, 'category__published': True}
    else:
        filters = {key: object_key, 'published': True, 'published': True}
    objs = object_type.objects.filter(**filters)
    if len(objs) == 0:
        filters = {key: object_key}
        objs = object_type.objects.filter(**filters)

    if len(objs) == 0:
        if create_if_not_exists:
            print_log('CREATING {0} (not found)...'.format(object_key))
            o = object_type()
            o.save()
            if 'name' not in params:
                params['name'] = object_key
            update_attributes([o,], params, log)
        else:
            log('{0} identified with {1} not found'.format(object_type, object_key))
    else:
        print_log('UPDATING {0}'.format(object_key))
        update_attributes(objs, params, log)
