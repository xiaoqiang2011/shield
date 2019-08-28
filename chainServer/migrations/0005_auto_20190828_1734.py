# Generated by Django 2.2.4 on 2019-08-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chainServer', '0004_auto_20190828_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recordnodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('ID_card', models.CharField(max_length=18)),
                ('money', models.FloatField(max_length=20)),
                ('funding_terms', models.IntegerField()),
                ('default_date', models.DateTimeField(max_length=50)),
                ('hash_previous', models.CharField(max_length=255)),
                ('hash_current', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='blocks',
        ),
    ]
