# Generated by Django 5.0.6 on 2024-07-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='required_param',
            name='Employment_Profile',
            field=models.CharField(choices=[(0, 'Freelancer'), (1, 'Salaried'), (2, 'Self-Employed'), (3, 'Student')], max_length=30),
        ),
        migrations.AlterField(
            model_name='required_param',
            name='Gender',
            field=models.CharField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='required_param',
            name='credit_history',
            field=models.CharField(choices=[(0, 'Bad'), (1, 'Neutral'), (2, 'Good')], max_length=30),
        ),
    ]
