# Generated by Django 2.2.4 on 2019-09-03 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shieldServer', '0011_auto_20190903_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrower',
            old_name='payback',
            new_name='loan_duration',
        ),
    ]