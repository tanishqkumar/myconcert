# Generated by Django 3.0.8 on 2020-08-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0008_boardentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardentry',
            name='num_cme_credits',
        ),
        migrations.AddField(
            model_name='boardentry',
            name='timeline',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
