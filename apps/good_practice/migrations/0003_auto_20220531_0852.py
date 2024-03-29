# Generated by Django 3.2.13 on 2022-05-31 08:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ("country", "0018_country_good_practice_region"),
        ("good_practice", "0002_alter_goodpractice_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "youtube_video_url",
                    models.URLField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Youtube video url",
                    ),
                ),
                (
                    "image",
                    models.FileField(
                        blank=True, upload_to="gallery/", verbose_name="Image"
                    ),
                ),
                (
                    "caption",
                    models.TextField(blank=True, null=True, verbose_name="Caption"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="Is published?"),
                ),
            ],
            options={
                "verbose_name": "Gallery",
                "verbose_name_plural": "Gallery",
            },
        ),
        migrations.RemoveField(
            model_name="goodpractice",
            name="country",
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="countries",
            field=models.ManyToManyField(
                related_name="country_good_practice",
                to="country.Country",
                verbose_name="Countries",
            ),
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2022, 5, 31, 8, 51, 44, 584019, tzinfo=utc),
                verbose_name="Created at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="end_year",
            field=models.BigIntegerField(
                blank=True, null=True, verbose_name="End year"
            ),
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="good_practice_form_url",
            field=models.URLField(
                default=datetime.datetime(2022, 5, 31, 8, 51, 47, 415631, tzinfo=utc),
                max_length=255,
                verbose_name="Good practice form URL",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="image",
            field=models.FileField(
                blank=True,
                upload_to="good_practice/",
                verbose_name="Good practice image",
            ),
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="media_and_resource_links",
            field=models.TextField(
                blank=True, null=True, verbose_name="Media and resource links"
            ),
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="page_viewed_count",
            field=models.BigIntegerField(
                default=0, verbose_name="Total page viewed count"
            ),
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="published_date",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2022, 5, 31, 8, 51, 51, 679316, tzinfo=utc),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="start_year",
            field=models.BigIntegerField(default=2022, verbose_name="Start year"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="goodpractice",
            name="drivers_of_displacement",
            field=models.CharField(
                choices=[
                    (
                        "increasing_temperatures_drought_and_desertification",
                        "Increasing temperatures, drought, and desertification",
                    ),
                    (
                        "land_forest_degradation_and_loss_of_biodiversity",
                        "Land/forest degradation and loss of biodiversity",
                    ),
                    (
                        "sea_level_rise_salinization_and_ocean_acidification",
                        "Sea level rise, salinization, and ocean acidification",
                    ),
                    ("glacial_melt", "Glacial melt"),
                    ("floods", "Floods"),
                    ("landslides", "Landslides"),
                ],
                max_length=255,
                verbose_name="Driver of displacement",
            ),
        ),
        migrations.AlterField(
            model_name="goodpractice",
            name="focus_area",
            field=models.CharField(
                choices=[
                    ("livelihoods_and_employment", "Livelihoods and employment"),
                    ("safety_and_security", "Safety and social security"),
                    ("health", "Health"),
                    ("education", "Education"),
                    ("housing_land_and_property", "Housing, land and property"),
                    ("environment", "Environment"),
                    ("food_and_water_insecurity", "Food and water insecurity"),
                    (
                        "social_protection_and_assistance",
                        "Social protection and assistance",
                    ),
                ],
                max_length=255,
                verbose_name="Focus area",
            ),
        ),
        migrations.AlterField(
            model_name="goodpractice",
            name="stage",
            field=models.CharField(
                blank=True,
                choices=[
                    ("promising", "Promising"),
                    ("advanced", "Advanced"),
                    ("successful", "Successful"),
                ],
                max_length=255,
                null=True,
                verbose_name="Stage",
            ),
        ),
        migrations.AlterField(
            model_name="goodpractice",
            name="type",
            field=models.CharField(
                choices=[
                    (
                        "risk_reduction_and_prevention",
                        "Risk Reduction and Prevention (DRR, CCA and peacebuilding)",
                    ),
                    (
                        "protection_and_assistance_and_durable_solutions",
                        "Protection and assistance, and durable solutions",
                    ),
                    (
                        "strengthening_policy_and_legal_frameworks",
                        "Strengthening policy and legal frameworks",
                    ),
                    ("interventions", "Interventions"),
                    ("policies", "Policies"),
                ],
                max_length=255,
                verbose_name="Good practice type",
            ),
        ),
        migrations.DeleteModel(
            name="MediaAndResourceLink",
        ),
        migrations.AddField(
            model_name="gallery",
            name="good_practice",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="good_practice",
                to="good_practice.goodpractice",
                verbose_name="Good practice",
            ),
        ),
    ]
