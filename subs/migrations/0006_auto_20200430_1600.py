# Generated by Django 2.2.12 on 2020-04-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0005_auto_20200429_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='credit_for',
            field=models.CharField(choices=[('ABS', 'American Board of Surgery'), ('ABMS', 'American Board of Medical Specialties')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='name',
            field=models.CharField(choices=[('NEJM', 'New England Journal of Medicine'), ('JVS', 'Journal of Vascular Surgery')], max_length=256),
        ),
        migrations.AlterField(
            model_name='membershipentry',
            name='credit_for',
            field=models.CharField(choices=[('ABS', 'American Board of Surgery'), ('ABMS', 'American Board of Medical Specialties')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='membershipentry',
            name='name',
            field=models.CharField(choices=[('ACS', 'American College of Surgeons'), ('AMA', 'American Medical Association')], max_length=256),
        ),
    ]
