# Generated by Django 3.2.13 on 2022-05-26 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0016_auto_20220518_0846'),
        ('good_practice', '0005_auto_20220526_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodpractice',
            name='country',
        ),
        migrations.AddField(
            model_name='goodpractice',
            name='countries',
            field=models.ManyToManyField(related_name='country_good_practice', to='country.Country', verbose_name='Countries'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_video_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Youtube video url')),
                ('image', models.FileField(blank=True, upload_to='gallery/', verbose_name='Good practices')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='Caption')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published?')),
                ('good_practice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='good_practice', to='good_practice.goodpractice', verbose_name='Good practice')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]