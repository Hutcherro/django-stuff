# Generated by Django 3.0.6 on 2020-06-07 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycode', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newitem',
            old_name='when_added',
            new_name='pub_date',
        ),
    ]