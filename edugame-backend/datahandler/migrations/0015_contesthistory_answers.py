# Generated by Django 3.2.5 on 2021-07-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahandler', '0014_alter_contesthistory_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contesthistory',
            name='answers',
            field=models.TextField(default='[]', null=True),
        ),
    ]
