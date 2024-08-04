# Generated by Django 5.0.6 on 2024-07-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_', '0003_credit_score_delete_required_param'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit_score',
            name='filename',
        ),
        migrations.AlterField(
            model_name='credit_score',
            name='file',
            field=models.FileField(max_length=150, upload_to='json_files/'),
        ),
    ]
