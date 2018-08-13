from django.db import models
from south.modelsinspector import add_introspection_rules


UNKNOWN_STRING = 'Unknown'

class CharField(models.CharField):

    description = "CharField with default values"

    def add_unknown(self, choices):
        if 0 not in choices:
            choices.append((0, UNKNOWN_STRING))

        return(choices)


    def __init__(self, *args, **kwargs):
        # Default values
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 2000

        if 'choices' in kwargs:
            kwargs['choices'] = self.add_unknown(kwargs['choices'])

        super(CharField, self).__init__(*args, **kwargs)
