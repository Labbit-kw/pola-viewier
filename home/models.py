from django.db import models
from django.urls import reverse
# Create your models here.


class Filter(models.Model):
    objects = models.Manager()
    id = models.IntegerField(auto_created = True, primary_key = True)
    name = models.CharField(max_length=50)
    mode = models.IntegerField()
    m1_ratio_0_f = models.IntegerField(blank=True, null=True)
    m1_ratio_90_f = models.IntegerField(blank=True, null=True)
    m2_ratio_0_f = models.IntegerField(blank=True, null=True)
    m2_ratio_x_f = models.IntegerField(blank=True, null=True)
    m2_ratio_90_f = models.IntegerField(blank=True, null=True)
    m99_fix_ratio_f = models.IntegerField(blank=True, null=True)
    m2_ratio_x_v = models.IntegerField(blank=True, null=True)
    cam_fr_rt = models.IntegerField(blank=True, null=True)
    m4_v1 = models.IntegerField(blank=True, null=True)
    m4_v2 = models.IntegerField(blank=True, null=True)
    m4_v3 = models.IntegerField(blank=True, null=True)
    m4_v4 = models.IntegerField(blank=True, null=True)
    m4_v5 = models.IntegerField(blank=True, null=True)
    m4_v6 = models.IntegerField(blank=True, null=True)
    m4_v7 = models.IntegerField(blank=True, null=True)
    m4_v8 = models.IntegerField(blank=True, null=True)
    m4_v9 = models.IntegerField(blank=True, null=True)
    m4_v10 = models.IntegerField(blank=True, null=True)
    m4_v11 = models.IntegerField(blank=True, null=True)
    m4_f1 = models.IntegerField(blank=True, null=True)
    m4_f2 = models.IntegerField(blank=True, null=True)
    m4_f3 = models.IntegerField(blank=True, null=True)
    m4_f4 = models.IntegerField(blank=True, null=True)
    m4_f5 = models.IntegerField(blank=True, null=True)
    m4_f6 = models.IntegerField(blank=True, null=True)
    m4_f7 = models.IntegerField(blank=True, null=True)
    m4_f8 = models.IntegerField(blank=True, null=True)
    m4_f9 = models.IntegerField(blank=True, null=True)
    m4_f10 = models.IntegerField(blank=True, null=True)
    m4_f11 = models.IntegerField(blank=True, null=True)
    m5_ratio_0_f = models.IntegerField(blank=True, null=True)
    m5_ratio_23_f = models.IntegerField(blank=True, null=True)
    m5_ratio_45_f = models.IntegerField(blank=True, null=True)
    m5_ratio_67_f = models.IntegerField(blank=True, null=True)
    m5_ratio_90_f = models.IntegerField(blank=True, null=True)
    m5_ratio_23_hv = models.IntegerField(db_column='m5_ratio_23_HV', blank=True, null=True)  # Field name made lowercase.
    m5_ratio_45_hv = models.IntegerField(db_column='m5_ratio_45_HV', blank=True, null=True)  # Field name made lowercase.
    m99_ratio_45_lv = models.IntegerField(db_column='m99_raito_45_LV', blank=True, null=True)  # Field name made lowercase.
    m5_ratio_67_hv = models.IntegerField(db_column='m5_ratio_67_HV', blank=True, null=True)  # Field name made lowercase.
    m99_ratio_67_lv = models.IntegerField(db_column='m99_raito_67_LV', blank=True, null=True)  # Field name made lowercase.
    ip_1 = models.CharField(max_length=24, blank=True, null=True)
    ip_2 = models.CharField(max_length=24, blank=True, null=True)
    ip_3 = models.CharField(max_length=24, blank=True, null=True)
    ip_4 = models.CharField(max_length=24, blank=True, null=True)
    gateway = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter'

    def __str__(self):
        return self.name