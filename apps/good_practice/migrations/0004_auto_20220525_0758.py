# Generated by Django 3.2.13 on 2022-05-25 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('good_practice', '0003_auto_20220524_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodpractice',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 7, 58, 51, 998320, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goodpractice',
            name='focus_area',
            field=models.CharField(choices=[('health', 'Health'), ('education', 'Education'), ('livelihoods_and_employment', 'Livelihoods and employment'), ('housing_land_and_property', 'Housing, land and property'), ('food_and_water_insecurity', 'Food and water insecurity'), ('social_protection_and_assistance', 'Social protection and assistance'), ('safety_and_security', 'Safety and social security'), ('civic_and_social_rights', 'Civic and social rights'), ('environment', 'Environment'), ('gender', 'Gender'), ('disability', 'Disability'), ('children_and_youth', 'Children and youth')], max_length=255, verbose_name='Focus area'),
        ),
    ]
