# Generated by Django 3.2.6 on 2021-08-11 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oil_grants', '0002_auto_20210809_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('status', models.CharField(choices=[("didn't start", 'не начался'), ('goes on', 'продолжается'), ('ended', 'завершился')], default="didn't start", max_length=15)),
                ('date_of_update', models.DateTimeField(auto_now=True)),
                ('date_of_add', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Конкурс',
                'verbose_name_plural': 'Конкурсы',
            },
        ),
        migrations.AddField(
            model_name='edprogram',
            name='date_of_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edprogram',
            name='date_of_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='grant',
            name='date_of_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grant',
            name='date_of_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='oilcompany',
            name='date_of_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oilcompany',
            name='date_of_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='programgroup',
            name='date_of_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programgroup',
            name='date_of_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='date_of_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='date_of_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='edprogram',
            name='p_name',
            field=models.CharField(max_length=150, verbose_name='Наименование ОП'),
        ),
        migrations.AlterField(
            model_name='programgroup',
            name='g_name',
            field=models.CharField(max_length=150, verbose_name='Наименование направления подготовки'),
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_passed', models.BooleanField(default=False)),
                ('date_of_update', models.DateTimeField(auto_now=True)),
                ('date_of_add', models.DateTimeField(auto_now_add=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='oil_grants.competitions')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.AddField(
            model_name='competitions',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='oil_grants.oilcompany'),
        ),
        migrations.AddField(
            model_name='competitions',
            name='ed_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='oil_grants.edprogram'),
        ),
    ]