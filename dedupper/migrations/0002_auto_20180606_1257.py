# Generated by Django 2.0.5 on 2018-06-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dedupper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simple',
            name='average',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simple',
            name='type',
            field=models.CharField(choices=[('U', 'Undecided'), ('D', 'Duplicated'), ('N', 'New Record')], default='U', max_length=128),
        ),
    ]