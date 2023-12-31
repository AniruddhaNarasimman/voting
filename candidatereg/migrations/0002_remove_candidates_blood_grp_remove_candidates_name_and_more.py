# Generated by Django 4.2.3 on 2023-07-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatereg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidates',
            name='blood_grp',
        ),
        migrations.RemoveField(
            model_name='candidates',
            name='name',
        ),
        migrations.RemoveField(
            model_name='candidates',
            name='rno',
        ),
        migrations.AddField(
            model_name='candidates',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidates',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='candidates',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidates',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidates',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidates',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='candidate_pics/'),
        ),
        migrations.AddField(
            model_name='candidates',
            name='roll_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidates',
            name='second_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
