# Generated by Django 4.0.5 on 2022-06-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_app', '0012_alter_candidateprofile_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='age',
            field=models.CharField(choices=[('16-20', '16-20'), ('21-30', '21-30'), ('31-40', '31-40'), ('40+', '40+')], max_length=20),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=20),
        ),
    ]
