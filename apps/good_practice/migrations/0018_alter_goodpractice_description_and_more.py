# Generated by Django 4.1.5 on 2023-05-31 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_practice', '0017_alter_goodpractice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodpractice',
            name='description',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Description of the project (max 2,000 characters)'),
        ),
        migrations.AlterField(
            model_name='goodpractice',
            name='description_en',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Description of the project (max 2,000 characters)'),
        ),
        migrations.AlterField(
            model_name='goodpractice',
            name='description_fr',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Description of the project (max 2,000 characters)'),
        ),
    ]
