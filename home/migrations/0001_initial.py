# Generated by Django 3.2.6 on 2021-08-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('mode', models.IntegerField()),
                ('m1_ratio_0_f', models.IntegerField(blank=True, null=True)),
                ('m1_ratio_90_f', models.IntegerField(blank=True, null=True)),
                ('m2_ratio_0_f', models.IntegerField(blank=True, null=True)),
                ('m2_ratio_x_f', models.IntegerField(blank=True, null=True)),
                ('m2_ratio_90_f', models.IntegerField(blank=True, null=True)),
                ('m99_fix_ratio_f', models.IntegerField(blank=True, null=True)),
                ('m2_ratio_x_v', models.IntegerField(blank=True, null=True)),
                ('cam_fr_rt', models.IntegerField(blank=True, null=True)),
                ('m4_v1', models.IntegerField(blank=True, null=True)),
                ('m4_v2', models.IntegerField(blank=True, null=True)),
                ('m4_v3', models.IntegerField(blank=True, null=True)),
                ('m4_v4', models.IntegerField(blank=True, null=True)),
                ('m4_v5', models.IntegerField(blank=True, null=True)),
                ('m4_v6', models.IntegerField(blank=True, null=True)),
                ('m4_v7', models.IntegerField(blank=True, null=True)),
                ('m4_v8', models.IntegerField(blank=True, null=True)),
                ('m4_v9', models.IntegerField(blank=True, null=True)),
                ('m4_v10', models.IntegerField(blank=True, null=True)),
                ('m4_v11', models.IntegerField(blank=True, null=True)),
                ('m4_f1', models.IntegerField(blank=True, null=True)),
                ('m4_f2', models.IntegerField(blank=True, null=True)),
                ('m4_f3', models.IntegerField(blank=True, null=True)),
                ('m4_f4', models.IntegerField(blank=True, null=True)),
                ('m4_f5', models.IntegerField(blank=True, null=True)),
                ('m4_f6', models.IntegerField(blank=True, null=True)),
                ('m4_f7', models.IntegerField(blank=True, null=True)),
                ('m4_f8', models.IntegerField(blank=True, null=True)),
                ('m4_f9', models.IntegerField(blank=True, null=True)),
                ('m4_f10', models.IntegerField(blank=True, null=True)),
                ('m4_f11', models.IntegerField(blank=True, null=True)),
                ('m5_ratio_0_f', models.IntegerField(blank=True, null=True)),
                ('m5_ratio_23_f', models.IntegerField(blank=True, null=True)),
                ('m5_ratio_45_f', models.IntegerField(blank=True, null=True)),
                ('m5_ratio_67_f', models.IntegerField(blank=True, null=True)),
                ('m5_ratio_90_f', models.IntegerField(blank=True, null=True)),
                ('m5_ratio_23_hv', models.IntegerField(blank=True, db_column='m5_ratio_23_HV', null=True)),
                ('m5_ratio_45_hv', models.IntegerField(blank=True, db_column='m5_ratio_45_HV', null=True)),
                ('m99_ratio_45_lv', models.IntegerField(blank=True, db_column='m99_raito_45_LV', null=True)),
                ('m5_ratio_67_hv', models.IntegerField(blank=True, db_column='m5_ratio_67_HV', null=True)),
                ('m99_ratio_67_lv', models.IntegerField(blank=True, db_column='m99_raito_67_LV', null=True)),
                ('ip_1', models.CharField(blank=True, max_length=24, null=True)),
                ('ip_2', models.CharField(blank=True, max_length=24, null=True)),
                ('ip_3', models.CharField(blank=True, max_length=24, null=True)),
                ('ip_4', models.CharField(blank=True, max_length=24, null=True)),
                ('gateway', models.CharField(blank=True, max_length=24, null=True)),
            ],
            options={
                'db_table': 'db_filter',
                'managed': False,
            },
        ),
    ]
