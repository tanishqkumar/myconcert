# Generated by Django 2.2.12 on 2020-04-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('renewal_date', models.DateField(verbose_name='Date of Renewal')),
                ('sub_cost', models.FloatField(blank=True, max_length=6)),
                ('poster_link', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('renewal_date', models.DateField(verbose_name='Date of Renewal')),
                ('sub_cost', models.FloatField(blank=True, max_length=6)),
                ('poster_link', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
