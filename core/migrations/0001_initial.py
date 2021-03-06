# Generated by Django 4.0.5 on 2022-06-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('event_data', models.DateTimeField()),
                ('creation_data', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]
