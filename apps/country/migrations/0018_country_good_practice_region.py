# Generated by Django 3.2.13 on 2022-05-31 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0017_alter_snapshotfile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='good_practice_region',
            field=models.CharField(blank=True, choices=[('the_americas', 'The Americas'), ('sub_saharan_africa', 'Sub-Saharan Africa'), ('south_asia', 'South Asia'), ('middle_east_and_north_africa', 'Middle East and North Africa'), ('east_asia_and_the_pacific', 'East Asia and the Pacific'), ('europe_and_central_asia', 'Europe and Central Asia')], max_length=100, null=True, verbose_name='Good practice region'),
        ),
    ]
