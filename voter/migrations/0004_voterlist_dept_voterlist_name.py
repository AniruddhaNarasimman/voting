# Generated by Django 4.2.3 on 2023-07-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0003_remove_voterlist_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='voterlist',
            name='dept',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='voterlist',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]