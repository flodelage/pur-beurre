# Generated by Django 3.2.9 on 2021-12-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20211213_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.URLField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(max_length=254),
        ),
    ]
