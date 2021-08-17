# Generated by Django 3.2.6 on 2021-08-13 07:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oil_grants', '0012_auto_20210813_0604'),
        ('users_app', '0004_alter_users_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='edProgram',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='oil_grants.edprogram'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gpa',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='users',
            name='receipt_date',
            field=models.DateField(null=True),
        ),
    ]