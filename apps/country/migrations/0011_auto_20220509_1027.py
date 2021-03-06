# Generated by Django 3.2.13 on 2022-05-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0010_auto_20220509_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essentiallink',
            name='country',
        ),
        migrations.AddField(
            model_name='country',
            name='contact_person_description',
            field=models.TextField(blank=True, null=True, verbose_name='Contact person description'),
        ),
        migrations.AddField(
            model_name='country',
            name='contact_person_image',
            field=models.FileField(blank=True, upload_to='contact_person/'),
        ),
        migrations.AddField(
            model_name='country',
            name='essential_links',
            field=models.TextField(blank=True, null=True, verbose_name='Essential links'),
        ),
        migrations.DeleteModel(
            name='ContactPerson',
        ),
        migrations.DeleteModel(
            name='EssentialLink',
        ),
    ]
