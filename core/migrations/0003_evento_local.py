# Generated by Django 4.0.5 on 2022-06-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_user_alter_evento_event_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
