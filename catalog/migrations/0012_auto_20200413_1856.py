# Generated by Django 3.0.3 on 2020-04-13 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20200413_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(1900)]),
        ),
    ]
