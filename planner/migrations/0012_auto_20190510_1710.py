# Generated by Django 2.2.1 on 2019-05-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0011_event_course_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='course',
            field=models.CharField(choices=[('NA', 'No Course')], default='No Course', max_length=10),
        ),
    ]
