# Generated by Django 4.1.3 on 2022-12-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0020_auto_20220911_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_fr',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
    ]
