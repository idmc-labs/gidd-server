# Generated by Django 4.1.4 on 2022-12-16 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0021_country_name_en_country_name_fr'),
    ]

    operations = [
        migrations.CreateModel(
            name='FigureAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='year')),
                ('crisis_type', models.CharField(choices=[('conflict', 'Conflict'), ('disaster', 'Disaster')], max_length=255, verbose_name='Crisis type')),
                ('nd_figures', models.BigIntegerField(verbose_name='New displacement figures')),
                ('nd_methodology_and_sources', models.TextField(blank=True, null=True, verbose_name='New displacement methodology and sources')),
                ('nd_caveats_and_challenges', models.TextField(blank=True, null=True, verbose_name='New displacement caveats and challenges')),
                ('idp_figures', models.BigIntegerField(verbose_name='Internal displacement figures')),
                ('idp_methodology_and_sources', models.TextField(blank=True, null=True, verbose_name='Internal displacment methodology and sources')),
                ('idp_caveats_and_challenges', models.TextField(blank=True, null=True, verbose_name='Internal displacment caveats and challenges')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='countries', to='country.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Figure analysis',
                'verbose_name_plural': 'Figures analysis',
                'unique_together': {('year', 'country', 'crisis_type')},
            },
        ),
    ]