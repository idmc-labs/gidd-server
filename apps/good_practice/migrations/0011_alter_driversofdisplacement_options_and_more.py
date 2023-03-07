# Generated by Django 4.1.4 on 2022-12-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("good_practice", "0010_auto_20221103_1132"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driversofdisplacement",
            options={
                "verbose_name": "Filters - Drivers of displacement",
                "verbose_name_plural": "Filters - Drivers of displacements",
            },
        ),
        migrations.AlterModelOptions(
            name="faq",
            options={
                "verbose_name": "HOMEPAGE - Frequently asked question",
                "verbose_name_plural": "HOMEPAGE - Frequently asked questions",
            },
        ),
        migrations.AlterModelOptions(
            name="focusarea",
            options={
                "verbose_name": "Filters - Focus area",
                "verbose_name_plural": "Filters - Focus areas",
            },
        ),
        migrations.AlterModelOptions(
            name="goodpractice",
            options={
                "verbose_name": "PAGES - Good practices page",
                "verbose_name_plural": "PAGES - Good practices pages",
            },
        ),
        migrations.AddField(
            model_name="goodpractice",
            name="is_public",
            field=models.BooleanField(
                default=False, editable=False, verbose_name="Is public?"
            ),
        ),
    ]
