"""Test Harvest tools

"""
from django.test import TestCase
#from unittest import skip
#from avocado.models import DataField, DataContext

class TestDbStructure(TestCase):
    """Tests the subject/record representation."""
    # fixtures = ['fixture.concepts.json']
    fixtures = ['fixture.auth_and_concepts.json']

    def test_renaaddme_concept(self):
        self.assertEqual(False, True, 'No timeline if no event')
