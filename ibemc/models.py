from django.db import models
from Subset1_normalized_models_coded_values import *
from Subset2_normalized_models_coded_values import *

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
    ## Subset 1
    ibemc_clinic = models.ForeignKey('v_intakedemographic_ibemc_clinic', help_text=u'', null=True, verbose_name=u'IBEMC center name', blank=True) # This field type is a guess
    u_consent_obtained = models.ForeignKey('v_intakedemographic_u_consent_obtained', max_length=2000, blank=True, help_text=u'1980 34 0 4661 0 FALSE', null=True, verbose_name=u'Consent obtained')
    u_assent_obtained = models.ForeignKey('v_intakedemographic_u_assent_obtained', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Assent obtained')
    u_societal_sex = models.ForeignKey('v_intakedemographic_u_societal_sex', help_text=u'', null=True, verbose_name=u'Societal sex ', blank=True) # This field type is a guess
    u_biological_sex = models.ForeignKey('v_intakedemographic_u_biological_sex', help_text=u'', null=True, verbose_name=u'Biological sex', blank=True) # This field type is a guess
    u_primary_language = models.ForeignKey('v_intakedemographic_u_primary_language', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Primary language spoken at home')
    u_recontact = models.ForeignKey('v_intakedemographic_u_recontact', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Permission to recontact')
    record = models.ForeignKey(Record)

    ## Subset 2
    u_cond_amino_acid = models.ForeignKey('v_intakedemographic_u_cond_amino_acid', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify amino acid disorder diagnosis for the patient')
    u_cond_faod = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify fatty acid oxidation disorder diagnosis for the patient', blank=True)
    u_cond_org_acid = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify organic acid disorder diagnosis for the patient', blank=True)
    u_cond_cand = models.ForeignKey('v_intakedemographic_u_cond_cand', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify SACHDNC  candidate disorder diagnosis for the patient')
    u_cond_not_listed = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify condition not listed for the patient', blank=True)

    class Meta:
	 db_table = 'intakedemographic'

## Subset 2
class upatientconditioncat(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patient condition category', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Patient condition category', choices=[(1, u'Amino acid disorders'), (2, u'Endocrine disorders'), (3, u'Fatty acid oxidation disorders'), (4, u'Hemoglobin disorders'), (5, u'Organic acid disorders'), (6, u'Other disorders'), (7, u'SACHDNC candidate disorders'), (8, u'Condition not listed')])
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'upatientconditioncat'


class ucondendo(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify endocrine disorder diagnosis for the patient', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify endocrine disorder diagnosis for the patient', choices=[(1, u'Congenital adrenal hyperplasia (CAH)'), (2, u'Primary congenital hypothyroidism (CH)')])
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'ucondendo'


class ucondhemo(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify hemoglobin disorder diagnosis for the patient', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify hemoglobin disorder diagnosis for the patient', choices=[(1, u'S beta-thalassemia (Hb S/bTh)'), (2, u'SC disease (Hb S/C)'), (3, u'SS disease (Sickle cell anemia) (Hb SS)'), (4, u'Various other hemoglobinopathies (Var Hb)')])
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'ucondhemo'


class ucondother(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify other diagnosis for the patient', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify other diagnosis for the patient', choices=[(1, u'Biotinidase deficiency (BIOT)'), (2, u'Critical congenital heart disease (CCHD)'), (3, u'Cystic fibrosis (CF)'), (4, u'Classic galactosemia (GALT)'), (5, u'Hearing loss (HEAR)'), (6, u'Severe combined immunodeficiences (SCID)'), (7, u'Galactoepimerase deficiency (GALE)'), (8, u'Galactokinase deficiency (GALK)'), (9, u'T-cell related lymphocyte deficiences')])
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'ucondother'


class VisitHealthHistory(models.Model):
    u_med_proc_i = models.ForeignKey('v_visithealthhistory_u_med_proc_i', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Major medical procedure since last visit')
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'visithealthhistory'

class VisitManagementAndTreatmentPharmacotherapy(models.Model):
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'visitmanagementandtreatmentpharmacotherapy'


## End Subset 2
