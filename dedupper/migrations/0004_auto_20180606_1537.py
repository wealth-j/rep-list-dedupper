# Generated by Django 2.0.5 on 2018-06-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dedupper', '0003_auto_20180606_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simple',
            name='type',
            field=models.CharField(choices=[('Undecided', 'Undecided'), ('Duplicate', 'Duplicate'), ('New Record', 'New Record')], default='Undecided', max_length=128),
        ),
    ]