from django.db import models

class v_intakedemographic_u_cond_amino_acid(models.Model):
   u_cond_amino_acid_v = models.TextField(verbose_name='Specify amino acid disorder diagnosis for the patient')
   class Meta:
      db_table = 'v_intakedemographic_u_cond_amino_acid'

class v_intakedemographic_u_cond_cand(models.Model):
   u_cond_cand_v = models.TextField(verbose_name='Specify SACHDNC  candidate disorder diagnosis for the patient')
   class Meta:
      db_table = 'v_intakedemographic_u_cond_cand'

class v_visithealthhistory_u_med_proc_i(models.Model):
   u_med_proc_i_v = models.TextField(verbose_name='Major medical procedure since last visit')
   class Meta:
      db_table = 'v_visithealthhistory_u_med_proc_i'
