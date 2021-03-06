# Generated by Django 2.2.12 on 2020-04-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0002_auto_20200429_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='credit_for',
            field=models.CharField(choices=[('ABS', 'American Board of Surgery'), ('ABMS', 'American Board of Medical Specialties')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='membershipentry',
            name='credit_for',
            field=models.CharField(choices=[('ABS', 'American Board of Surgery'), ('ABMS', 'American Board of Medical Specialties')], max_length=256, null=True),
        ),
    ]
