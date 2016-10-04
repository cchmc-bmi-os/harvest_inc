from django.db import models


class Fieldstats(models.Model):
    dataset = models.CharField(help_text=u'Dataset containing the fields', max_length = 1024)
    field_name = models.CharField(help_text=u'Redcap field name', max_length = 1024)
    field_label = models.CharField(help_text=u'Field Label', max_length = 1024)
    ep = models.IntegerField(help_text=u'ExpeCted Present')
    ea = models.IntegerField(help_text=u'Expected Absent')
    np = models.IntegerField(help_text=u'Non expexted Present')
    na = models.IntegerField(help_text=u'Non expexted Absent')
    fa = models.IntegerField(help_text=u'Field Absent')
    nu = models.IntegerField(help_text=u'Never Utilized')

    class Meta:
	 db_table = 'fieldstats'
