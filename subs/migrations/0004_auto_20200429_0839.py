# Generated by Django 2.2.12 on 2020-04-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0003_auto_20200429_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='cme_available',
            field=models.DateField(blank=True, null=True, verbose_name='CME Available'),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='renewal_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Renewal'),
        ),
        migrations.AlterField(
            model_name='membershipentry',
            name='cme_available',
            field=models.DateField(blank=True, null=True, verbose_name='CME Available'),
        ),
        migrations.AlterField(
            model_name='membershipentry',
            name='renewal_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Renewal'),
        ),
    ]
