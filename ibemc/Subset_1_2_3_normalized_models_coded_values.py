from django.db import models

class v_intakedemographic_biopt_bs_diag_des(models.Model):
   biopt_bs_diag_des_v = models.TextField(verbose_name='BIOPT-BS Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_biopt_bs_diag_des'

class v_intakedemographic_biopt_reg_diag_des(models.Model):
   biopt_reg_diag_des_v = models.TextField(verbose_name='BIOPT-REG Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_biopt_reg_diag_des'

class v_intakedemographic_biot_diag_des(models.Model):
   biot_diag_des_v = models.TextField(verbose_name='BIOT Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_biot_diag_des'

class v_intakedemographic_cpt2_diag_des(models.Model):
   cpt2_diag_des_v = models.TextField(verbose_name='CPT-II Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_cpt2_diag_des'

class v_intakedemographic_gale_diag_des(models.Model):
   gale_diag_des_v = models.TextField(verbose_name='GALE Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_gale_diag_des'

class v_intakedemographic_galt_diag_des(models.Model):
   galt_diag_des_v = models.TextField(verbose_name='GALT Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_galt_diag_des'

class v_intakedemographic_hcy_diag_des(models.Model):
   hcy_diag_des_v = models.TextField(verbose_name='HCY Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_hcy_diag_des'

class v_intakedemographic_ibemc_clinic(models.Model):
   ibemc_clinic_v = models.TextField(verbose_name='IBEMC center name')
   class Meta:
      db_table = 'v_intakedemographic_ibemc_clinic'

class v_intakedemographic_mga_diag_des(models.Model):
   mga_diag_des_v = models.TextField(verbose_name='3MGA Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_mga_diag_des'

class v_intakedemographic_mhcy_diag_des(models.Model):
   mhcy_diag_des_v = models.TextField(verbose_name='CblC,D Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_mhcy_diag_des'

class v_intakedemographic_mma_diag_des(models.Model):
   mma_diag_des_v = models.TextField(verbose_name='CblA,B Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_mma_diag_des'

class v_intakedemographic_msud_diag_des(models.Model):
   msud_diag_des_v = models.TextField(verbose_name='MSUD Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_msud_diag_des'

class v_intakedemographic_mut_diag_des(models.Model):
   mut_diag_des_v = models.TextField(verbose_name='MUT Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_mut_diag_des'

class v_intakedemographic_pku_diag_des(models.Model):
   pku_diag_des_v = models.TextField(verbose_name='PKU Diagnosis')
   class Meta:
      db_table = 'v_intakedemographic_pku_diag_des'

class v_intakedemographic_u_assent_obtained(models.Model):
   u_assent_obtained_v = models.TextField(verbose_name='Assent obtained')
   class Meta:
      db_table = 'v_intakedemographic_u_assent_obtained'

class v_intakedemographic_u_biological_sex(models.Model):
   u_biological_sex_v = models.TextField(verbose_name='Biological sex')
   class Meta:
      db_table = 'v_intakedemographic_u_biological_sex'

class v_intakedemographic_u_cond_endo(models.Model):
   u_cond_endo_v = models.TextField(verbose_name='Specify endocrine disorder diagnosis for the patient')
   class Meta:
      db_table = 'v_intakedemographic_u_cond_endo'

class v_intakedemographic_u_cond_hemo(models.Model):
   u_cond_hemo_v = models.TextField(verbose_name='Specify hemoglobin disorder diagnosis for the patient')
   class Meta:
      db_table = 'v_intakedemographic_u_cond_hemo'

class v_intakedemographic_u_cond_other(models.Model):
   u_cond_other_v = models.TextField(verbose_name='Specify other diagnosis for the patient')
   class Meta:
      db_table = 'v_intakedemographic_u_cond_other'

class v_intakedemographic_u_consent_obtained(models.Model):
   u_consent_obtained_v = models.TextField(verbose_name='Consent obtained')
   class Meta:
      db_table = 'v_intakedemographic_u_consent_obtained'

class v_intakedemographic_u_primary_language(models.Model):
   u_primary_language_v = models.TextField(verbose_name='Primary language spoken at home')
   class Meta:
      db_table = 'v_intakedemographic_u_primary_language'

class v_intakedemographic_u_recontact(models.Model):
   u_recontact_v = models.TextField(verbose_name='Permission to recontact')
   class Meta:
      db_table = 'v_intakedemographic_u_recontact'

class v_intakedemographic_u_societal_sex(models.Model):
   u_societal_sex_v = models.TextField(verbose_name='Societal sex ')
   class Meta:
      db_table = 'v_intakedemographic_u_societal_sex'

class v_studystatu_cond_fu_inactive(models.Model):
   cond_fu_inactive_v = models.TextField(verbose_name='Reason for inactive status')
   class Meta:
      db_table = 'v_studystatu_cond_fu_inactive'

class v_sitdemographicsandhistory_u_reconsent_i(models.Model):
   u_reconsent_i_v = models.TextField(verbose_name='Patient consent valid')
   class Meta:
      db_table = 'v_sitdemographicsandhistory_u_reconsent_i'

class v_visithealthhistory_u_med_proc_i(models.Model):
   u_med_proc_i_v = models.TextField(verbose_name='Major medical procedure since last visit')
   class Meta:
      db_table = 'v_visithealthhistory_u_med_proc_i'
