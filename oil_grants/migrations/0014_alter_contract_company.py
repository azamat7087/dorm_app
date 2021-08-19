# Generated by Django 3.2.6 on 2021-08-19 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oil_grants', '0013_auto_20210819_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='company',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='oil_grants.company', verbose_name='Компания спонсор'),
        ),
    ]
