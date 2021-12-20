# Generated by Django 3.2.9 on 2021-12-20 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('nutriscore', models.CharField(max_length=1)),
                ('nutrients', models.JSONField(default=dict)),
                ('brand', models.CharField(max_length=254, null=True)),
                ('description', models.TextField(null=True)),
                ('store', models.CharField(max_length=254, null=True)),
                ('picture', models.URLField(max_length=300, null=True)),
                ('url', models.URLField(max_length=300)),
                ('categories', models.ManyToManyField(related_name='products', to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_as_product', to='catalog.product')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_as_substitute', to='catalog.product')),
            ],
            options={
                'unique_together': {('substitute', 'product', 'profile')},
            },
        ),
    ]
