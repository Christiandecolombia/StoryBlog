# Generated by Django 3.0.1 on 2020-01-05 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lname',
            new_name='lastName',
        ),
    ]
