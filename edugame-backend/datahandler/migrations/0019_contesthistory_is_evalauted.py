# Generated by Django 3.2.5 on 2021-07-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0018_rename_percentagee_of_correct_answers_contesthistory_percentage_of_correct_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='contesthistory',
            name='is_evalauted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
