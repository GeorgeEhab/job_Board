# Generated by Django 3.1.7 on 2021-07-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0006_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
