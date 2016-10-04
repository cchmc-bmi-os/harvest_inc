from django.db import models
from Subset1_normalized_models_coded_values import *

class Subject(models.Model):
    ibemc_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IBEMC ID', blank=True)
    u_study_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IBEM-IS ID', blank=True)
    nb_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of records')
    nb_complete_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of complete visits')
    nb_valid_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of valid visits')

    class Meta:
	 db_table = 'subject'


class Record(models.Model):
    u_study_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IBEM-IS ID', blank=True)
    redcap_event_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Redcap Event Name', blank=True)
    event_type = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Event type', blank=True)
    intake_demographics_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Intake Demographics Complete")
    intake_family_history_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Intake Family History Complete")
    intake_past_health_history_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Intake Past Health History Complete")
    intake_newborn_screening_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Intake Newborn Screening Complete")
    intake_initial_testing_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Intake Initial Testing Complete")
    visit_demographics_and_history_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Visit Demographicsand History complete")
    visit_health_history_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Visit Healthhistory Complete")
    visit_findings_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Visit Findings Complete")
    visit_ancillary_care_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Visit Ancillarycare Complete")
    visit_lab_studies_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Visit Labstudies Complete")
    visit_studies_other_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Visit Studiesother Complete")
    visit_management_and_treatment_pharmacotherapy_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Visit Management and Treatment Pharmacotherapy Complete")
    visit_management_and_treatment_nutrition_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Visit Management and Treatment Nutrition Complete")
    study_status_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Study Status Complete")
    pregnancy_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Pregnancy Complete")
    dialysis_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Dialysis Complete")
    transplant_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Transplant Complete")
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
	 db_table = 'record'


class IntakeDemographic(models.Model):
    ibemc_clinic = models.ForeignKey('v_intakedemographic_ibemc_clinic', help_text=u'', null=True, verbose_name=u'IBEMC center name', blank=True) # This field type is a guess
    u_consent_obtained = models.ForeignKey('v_intakedemographic_u_consent_obtained', max_length=2000, blank=True, help_text=u'1980 34 0 4661 0 FALSE', null=True, verbose_name=u'Consent obtained')
    u_assent_obtained = models.ForeignKey('v_intakedemographic_u_assent_obtained', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Assent obtained')
    u_societal_sex = models.ForeignKey('v_intakedemographic_u_societal_sex', help_text=u'', null=True, verbose_name=u'Societal sex ', blank=True) # This field type is a guess
    u_biological_sex = models.ForeignKey('v_intakedemographic_u_biological_sex', help_text=u'', null=True, verbose_name=u'Biological sex', blank=True) # This field type is a guess
    u_primary_language = models.ForeignKey('v_intakedemographic_u_primary_language', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Primary language spoken at home')
    u_recontact = models.ForeignKey('v_intakedemographic_u_recontact', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Permission to recontact')
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'intakedemographic'
