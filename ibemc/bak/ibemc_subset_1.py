from django.db import models

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
