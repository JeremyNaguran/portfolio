# Generated by Django 2.2.24 on 2021-09-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_job_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
