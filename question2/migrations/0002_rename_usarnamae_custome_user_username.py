# Generated by Django 5.1.1 on 2024-09-14 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custome_user',
            old_name='usarnamae',
            new_name='username',
        ),
    ]
