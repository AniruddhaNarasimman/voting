# Generated by Django 4.2.3 on 2023-07-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatereg', '0003_alter_candidates_department_alter_candidates_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
