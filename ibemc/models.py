from django.db import models
from  Subset_1_2_3_normalized_models_coded_values import *

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


## Subset 1 2 3
class IntakeDemographic(models.Model):
    biopt_bs_diag_des = models.ForeignKey('v_intakedemographic_biopt_bs_diag_des', help_text=u'', null=True, verbose_name=u'BIOPT-BS Diagnosis', blank=True) # This field type is a guess
    biopt_reg_diag_des = models.ForeignKey('v_intakedemographic_biopt_reg_diag_des', help_text=u'', null=True, verbose_name=u'BIOPT-REG Diagnosis', blank=True) # This field type is a guess
    biot_diag_des = models.ForeignKey('v_intakedemographic_biot_diag_des', help_text=u'', null=True, verbose_name=u'BIOT Diagnosis', blank=True) # This field type is a guess
    cpt2_diag_des = models.ForeignKey('v_intakedemographic_cpt2_diag_des', help_text=u'', null=True, verbose_name=u'CPT-II Diagnosis', blank=True) # This field type is a guess
    gale_diag_des = models.ForeignKey('v_intakedemographic_gale_diag_des', help_text=u'', null=True, verbose_name=u'GALE Diagnosis', blank=True) # This field type is a guess
    galt_diag_des = models.ForeignKey('v_intakedemographic_galt_diag_des', help_text=u'', null=True, verbose_name=u'GALT Diagnosis', blank=True) # This field type is a guess
    hcy_diag_des = models.ForeignKey('v_intakedemographic_hcy_diag_des', help_text=u'', null=True, verbose_name=u'HCY Diagnosis', blank=True) # This field type is a guess
    ibemc_clinic = models.ForeignKey('v_intakedemographic_ibemc_clinic', help_text=u'', null=True, verbose_name=u'IBEMC center name', blank=True) # This field type is a guess
    mga_diag_des = models.ForeignKey('v_intakedemographic_mga_diag_des', help_text=u'', null=True, verbose_name=u'3MGA Diagnosis', blank=True) # This field type is a guess
    mhcy_diag_des = models.ForeignKey('v_intakedemographic_mhcy_diag_des', help_text=u'', null=True, verbose_name=u'CblC,D Diagnosis', blank=True) # This field type is a guess
    mma_diag_des = models.ForeignKey('v_intakedemographic_mma_diag_des', help_text=u'', null=True, verbose_name=u'CblA,B Diagnosis', blank=True) # This field type is a guess
    msud_diag_des = models.ForeignKey('v_intakedemographic_msud_diag_des', help_text=u'', null=True, verbose_name=u'MSUD Diagnosis', blank=True) # This field type is a guess
    mut_diag_des = models.ForeignKey('v_intakedemographic_mut_diag_des', help_text=u'', null=True, verbose_name=u'MUT Diagnosis', blank=True) # This field type is a guess
    pku_diag_des = models.ForeignKey('v_intakedemographic_pku_diag_des', help_text=u'', null=True, verbose_name=u'PKU Diagnosis', blank=True) # This field type is a guess
    u_age = models.FloatField(help_text=u'[u_dob]', null=True, verbose_name=u'Age', blank=True)
    u_assent_obtained = models.ForeignKey('v_intakedemographic_u_assent_obtained', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Assent obtained')
    u_biological_sex = models.ForeignKey('v_intakedemographic_u_biological_sex', help_text=u'', null=True, verbose_name=u'Biological sex', blank=True) # This field type is a guess
    u_cond_endo = models.ForeignKey('v_intakedemographic_u_cond_endo', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify endocrine disorder diagnosis for the patient')
    u_cond_hemo = models.ForeignKey('v_intakedemographic_u_cond_hemo', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify hemoglobin disorder diagnosis for the patient')
    u_cond_not_listed = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify condition not listed for the patient', blank=True)
    u_cond_other = models.ForeignKey('v_intakedemographic_u_cond_other', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify other diagnosis for the patient')
    u_consent_obtained = models.ForeignKey('v_intakedemographic_u_consent_obtained', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Consent obtained')
    u_dob = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of birth', blank=True)
    u_e_visit_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Intake date', blank=True)
    u_primary_language = models.ForeignKey('v_intakedemographic_u_primary_language', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Primary language spoken at home')
    u_recontact = models.ForeignKey('v_intakedemographic_u_recontact', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Permission to recontact')
    u_societal_sex = models.ForeignKey('v_intakedemographic_u_societal_sex', help_text=u'', null=True, verbose_name=u'Societal sex ', blank=True) # This field type is a guess
    u_study_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IBEM-IS ID', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'intakedemographic'


class ucondaminoacid(models.Model):
    ucondaminoacid = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify amino acid disorder diagnosis for the patient', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify amino acid disorder diagnosis for the patient', choices=[(1, u'Argininemia (ARG)'), (2, u'Argininosuccinic aciduria (ASA)'), (3, u'Benign Hyperphenylalaninemia (H-PHE)'), (4, u'Biopterin defect in cofactor biosynthesis (BIOPT BS)'), (5, u'Biopterin defect in cofactor regeneration (BIOPT REG)'), (6, u'Citrullinemia type I (CIT)'), (7, u'Citrullinemia type II (CIT II)'), (8, u'Classic Phenylketonuria (PKU)'), (9, u'Homocystinuria (HCY)'), (10, u'Hypermethioninemia (MET)'), (11, u'Maple syrup urine disease (MSUD)'), (12, u'Tyrosinemia type I (TYR I)'), (13, u'Tyrosinemia type II (TYR II)'), (14, u'Tyrosinemia type III (TYR III)')])
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'ucondaminoacid'


class ucondcand(models.Model):
    ucondcand = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify SACHDNC  candidate disorder diagnosis for the patient', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify SACHDNC  candidate disorder diagnosis for the patient', choices=[(1, u'Spinal muscular atrophy (SMA)')])
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'ucondcand'


class ucondfaod(models.Model):
    ucondfaod = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify fatty acid oxidation disorder diagnosis for the patient', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Specify fatty acid oxidation disorder diagnosis for the patient', choices=[(1, u'2- 4-Dienoyl-CoA reductase deficiency (DE RED)'), (2, u'Carnitine acylcarnitine translocase deficiency (CACT)'), (3, u'Carnitine palmitoyltransferase type I deficiency (CPT IA)'), (4, u'Carnitine palmitoyltransferase type II deficiency (CPT II)'), (5, u'Carnitine uptake defect/carnitine transport defect (CUD)'), (6, u'Glutaric acidemia type II (GA2)'), (7, u'Long-chain L-3 hydroxyacyl-CoA dehydrogenase deficiency (LCHAD)'), (8, u'Medium-chain acyl-CoA dehydrogenase deficiency (MCAD)'), (9, u'Medium-chain ketoacyl-CoA thiolase deficiency (MCAT)'), (10, u'Medium/short-chain L-3-hydroxyacyl-CoA dehydrogenase deficiency (M/SCHAD)'), (11, u'Short-chain acyl-CoA dehydrogenase deficiency (SCAD)'), (12, u'Trifunctional protein deficiency (TFP)'), (13, u'Very long-chain acyl-CoA dehydrogenase deficiency (VLCAD)')])
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'ucondfaod'


class ucondorgacid(models.Model):
    ucondorgacid = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify organic acid disorder diagnosis for the patient', blank=True)
    value = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify organic acid disorder diagnosis for the patient', blank=True)
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'ucondorgacid'


class upatientconditioncat(models.Model):
    upatientconditioncat = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patient condition category', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Patient condition category', choices=[(1, u'Amino acid disorders'), (2, u'Endocrine disorders'), (3, u'Fatty acid oxidation disorders'), (4, u'Hemoglobin disorders'), (5, u'Organic acid disorders'), (6, u'Other disorders'), (7, u'SACHDNC candidate disorders'), (8, u'Condition not listed')])
    intakedemographic = models.ForeignKey(IntakeDemographic)

    class Meta:
	 db_table = 'upatientconditioncat'


class IntakeNewbornScreening(models.Model):
    u_age_prim_notify = models.IntegerField(help_text=u'', null=True, verbose_name=u'Days of age from birth primary or subspecialist first notified about abnormal NBS screen', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'intakenewbornscreening'


class IntakePastHealthHistory(models.Model):
    u_age_fst_subspec = models.IntegerField(help_text=u'', null=True, verbose_name=u'Days of age from birth until first seen by subspecialist', blank=True)
    u_age_intervention = models.IntegerField(help_text=u'', null=True, verbose_name=u'Days of age from birth until intervention for this condition', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'intakepasthealthhistory'


class StudyStatu(models.Model):
    cond_fu_inactive_2 = models.ForeignKey('v_studystatu_cond_fu_inactive', related_name='cond_fu_inative_2', help_text=u'', null=True, verbose_name=u'Reason for inactive status 2', blank=True) # This field type is a guess
    cond_fu_inactive_3 = models.ForeignKey('v_studystatu_cond_fu_inactive', related_name='cond_fu_inative_3', help_text=u'', null=True, verbose_name=u'Reason for inactive status 3', blank=True) # This field type is a guess
    cond_fu_inactive_4 = models.ForeignKey('v_studystatu_cond_fu_inactive', related_name='cond_fu_inative_4', help_text=u'', null=True, verbose_name=u'Reason for inactive status 4', blank=True) # This field type is a guess
    cond_fu_inactive = models.ForeignKey('v_studystatu_cond_fu_inactive', help_text=u'', null=True, verbose_name=u'Reason for inactive status', blank=True) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'studystatu'


class VisitDemographicsAndHistory(models.Model):
    u_reconsent_i = models.ForeignKey('v_sitdemographicsandhistory_u_reconsent_i', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Patient consent valid')
    u_reconsent_prompt_i = models.TextField(help_text=u'', null=True, verbose_name=u'Obtain new consent prior to completing data entry.', blank=True) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'visitdemographicsandhistory'


class VisitHealthHistory(models.Model):
    u_med_proc_i = models.ForeignKey('v_visithealthhistory_u_med_proc_i', max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Major medical procedure since last visit')
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'visithealthhistory'


class VisitManagementAndTreatmentPharmacotherapy(models.Model):
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'visitmanagementandtreatmentpharmacotherapy'
## End Subset 1 2 3
