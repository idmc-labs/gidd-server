# Generated by Django 3.2.13 on 2022-05-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_practice', '0006_auto_20220526_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodpractice',
            name='drivers_of_dispalcement',
            field=models.CharField(choices=[('increasing_temperatures_drought_and_desertification', 'Increasing temperatures, drought, and desertification'), ('land_forest_degradation_and_loss_of_biodiversity', 'Land/forest degradation and loss of biodiversity'), ('sea_level_rise_salinization_and_ocean_acidification', 'Sea level rise, salinization, and ocean acidification'), ('glacial_melt', 'Glacial melt'), ('floods', 'Floods'), ('landslides', 'Landslides')], max_length=255, verbose_name='Driver of displacement'),
        ),
        migrations.AlterField(
            model_name='goodpractice',
            name='stage',
            field=models.CharField(blank=True, choices=[('promising', 'Promising'), ('advanced', 'Advanced'), ('successful', 'Successful')], max_length=255, null=True, verbose_name='Stage'),
        ),
        migrations.AlterField(
            model_name='goodpractice',
            name='type',
            field=models.CharField(choices=[('risk_reduction_and_prevention', 'Risk Reduction and Prevention (DRR, CCA and peacebuilding)'), ('protection_and_assistance_and_durable_solutions', 'Protection and assistance, and durable solutions'), ('strengthening_policy_and_legal_frameworks', 'Strengthening policy and legal frameworks'), ('interventions', 'Interventions'), ('policies', 'Policies')], max_length=255, verbose_name='Good practice type'),
        ),
    ]