# Generated by Django 3.2.12 on 2022-03-28 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryAdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_displacement', models.BigIntegerField(blank=True, null=True)),
                ('total_displacement_since', models.TextField(blank=True, null=True)),
                ('total_displacement_source', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'CountryAdditional Info',
                'verbose_name_plural': 'CountryAdditional Infos',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('iso3', models.CharField(max_length=10, verbose_name='Iso3')),
                ('iso2', models.CharField(max_length=255, verbose_name='Iso2')),
                ('idmc_names', models.CharField(blank=True, max_length=255, null=True, verbose_name='Idmc names')),
                ('idmc_continent', models.CharField(blank=True, choices=[('europe', 'Europe'), ('oceania', 'Oceania'), ('americas', 'Americas'), ('africa', 'Africa'), ('asia', 'Asia'), ('Antarctica', 'Antarctica')], max_length=100, null=True, verbose_name='Idmc continent')),
                ('idmc_region', models.CharField(blank=True, choices=[('caribbean', 'Caribbean'), ('south-east-asia', 'South-East Asia'), ('southern_europe', 'Southern Europe'), ('east_asia', 'East Asia'), ('north_america', 'North America'), ('south_asia', 'South Asia'), ('latin_america', 'Latin America'), ('western_africa', 'Western Africa'), ('micronesia', 'Micronesia'), ('horn_of_africa', 'Horn of Africa'), ('north_west_and_central_europe', 'North, West and Central Europe'), ('melanesia', 'Melanesia'), ('eastern_europe', 'Eastern Europe'), ('australia_and_nz', 'Australia and NZ'), ('central_africa', 'Central Africa'), ('polynesia', 'Polynesia'), ('northern_africa', 'Northern Africa'), ('central_asia', 'Central Asia'), ('western_asia', 'Western Asia'), ('southern-africa', 'Southern Africa')], max_length=100, null=True, verbose_name='Idmc region')),
                ('idmc_sub_region', models.CharField(blank=True, choices=[('south-caucasus', 'South Caucasus'), ('latin-america', 'Latin America'), ('middle-east', 'Middle East')], max_length=100, null=True, verbose_name='Idmc sub region')),
                ('wb_region', models.CharField(blank=True, choices=[('caribbean', 'Caribbean'), ('south-east-asia', 'South-East Asia'), ('southern_europe', 'Southern Europe'), ('east_asia', 'East Asia'), ('north_america', 'North America'), ('south_asia', 'South Asia'), ('latin_america', 'Latin America'), ('western_africa', 'Western Africa'), ('micronesia', 'Micronesia'), ('horn_of_africa', 'Horn of Africa'), ('north_west_and_central_europe', 'North, West and Central Europe'), ('melanesia', 'Melanesia'), ('eastern_europe', 'Eastern Europe'), ('australia_and_nz', 'Australia and NZ'), ('central_africa', 'Central Africa'), ('polynesia', 'Polynesia'), ('northern_africa', 'Northern Africa'), ('central_asia', 'Central Asia'), ('western_asia', 'Western Asia'), ('southern-africa', 'Southern Africa')], max_length=100, null=True, verbose_name='Wb region')),
                ('un_population_division_names', models.CharField(blank=True, max_length=255, null=True, verbose_name='Unpopulation division name')),
                ('united_nations_region', models.CharField(blank=True, choices=[('caribbean', 'Caribbean'), ('south-east-asia', 'South-East Asia'), ('southern_europe', 'Southern Europe'), ('east_asia', 'East Asia'), ('north_america', 'North America'), ('south_asia', 'South Asia'), ('latin_america', 'Latin America'), ('western_africa', 'Western Africa'), ('micronesia', 'Micronesia'), ('horn_of_africa', 'Horn of Africa'), ('north_west_and_central_europe', 'North, West and Central Europe'), ('melanesia', 'Melanesia'), ('eastern_europe', 'Eastern Europe'), ('australia_and_nz', 'Australia and NZ'), ('central_africa', 'Central Africa'), ('polynesia', 'Polynesia'), ('northern_africa', 'Northern Africa'), ('central_asia', 'Central Asia'), ('western_asia', 'Western Asia'), ('southern-africa', 'Southern Africa')], max_length=100, null=True, verbose_name='United nations region')),
                ('is_least_developed_country', models.BooleanField(default=False, verbose_name='Is least developed country?')),
                ('is_small_island_developing_state', models.BooleanField(default=False, verbose_name='Is small island developing state?')),
                ('is_idmc_go_2013', models.BooleanField(default=False, verbose_name='Is idmc go 2013?')),
                ('is_conflict_affected_since_1970', models.BooleanField(default=False, verbose_name='Is conflict affected since 1970?')),
                ('is_country_office_nrc', models.BooleanField(default=False, verbose_name='Is country office nrc?')),
                ('is_country_office_iom', models.BooleanField(default=False, verbose_name='Is country office iom?')),
                ('additional_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.countryadditionalinfo', verbose_name='Additional info')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]