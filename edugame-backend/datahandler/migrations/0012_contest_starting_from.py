# Generated by Django 3.2.5 on 2021-07-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0011_contest_point_to_deduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='starting_from',
            field=models.DateTimeField(null=True),
        ),
    ]
