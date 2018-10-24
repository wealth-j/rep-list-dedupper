# Generated by Django 2.0.5 on 2018-10-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dedupper', '0002_auto_20181010_0500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='completed',
            new_name='completed_keys',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='total',
            new_name='completed_reps',
        ),
        migrations.AddField(
            model_name='progress',
            name='total_reps',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
