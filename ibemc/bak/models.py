from django.db import models

class subject(models.Model):
    ibemc_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IBEMC ID', blank=True)
    u_study_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IBEM-IS ID', blank=True)
    nb_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of records')
    nb_complete_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of complete visits')
    nb_valid_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of valid visits')

    class Meta:
	 db_table = 'subject'


class Record(models.Model):
    subject = models.ForeignKey("subject")
    ## redcap_event_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Redcap Event Name', blank=True)

    class Meta:
        db_table = 'record'


class IntakeDemographic(models.Model):
    u_study_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IBEM-IS ID', blank=True)
    ibemc_clinic = models.ForeignKey('v_intakedemographic_ibemc_clinic')
    u_consent_obtained = models.ForeignKey('v_intakedemographic_u_consent_obtained')
    u_assent_obtained = models.ForeignKey('v_intakedemographic_u_assent_obtained')
    u_societal_sex = models.ForeignKey('v_intakedemographic_u_societal_sex')
    u_biological_sex = models.ForeignKey('v_intakedemographic_u_biological_sex')
    u_primary_language = models.ForeignKey('v_intakedemographic_u_primary_language')
    u_recontact = models.ForeignKey('v_intakedemographic_u_recontact')
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'intakedemographic'


class v_intakedemographic_ibemc_clinic(models.Model):
   ibemc_clinic_v = models.TextField(verbose_name='IBEMC center name')
   class Meta:
      db_table = 'v_intakedemographic_ibemc_clinic'

class v_intakedemographic_u_consent_obtained(models.Model):
   u_consent_obtained_v = models.TextField(verbose_name='Consent obtained')
   class Meta:
      db_table = 'v_intakedemographic_u_consent_obtained'

class v_intakedemographic_u_assent_obtained(models.Model):
   u_assent_obtained_v = models.TextField(verbose_name='Assent obtained')
   class Meta:
      db_table = 'v_intakedemographic_u_assent_obtained'

class v_intakedemographic_u_societal_sex(models.Model):
   u_societal_sex_v = models.TextField(verbose_name='Societal sex ')
   class Meta:
      db_table = 'v_intakedemographic_u_societal_sex'

class v_intakedemographic_u_biological_sex(models.Model):
   u_biological_sex_v = models.TextField(verbose_name='Biological sex')
   class Meta:
      db_table = 'v_intakedemographic_u_biological_sex'

class v_intakedemographic_u_primary_language(models.Model):
   u_primary_language_v = models.TextField(verbose_name='Primary language spoken at home')
   class Meta:
      db_table = 'v_intakedemographic_u_primary_language'

class v_intakedemographic_u_recontact(models.Model):
   u_recontact_v = models.TextField(verbose_name='Permission to recontact')
   class Meta:
      db_table = 'v_intakedemographic_u_recontact'
