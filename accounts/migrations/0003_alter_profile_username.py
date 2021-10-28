# Generated by Django 3.2.4 on 2021-10-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(error_messages={'unique': 'Un utilisateur avec ce nom existe déjà.'}, max_length=128, unique=True),
        ),
    ]
