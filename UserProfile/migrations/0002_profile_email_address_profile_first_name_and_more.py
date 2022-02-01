# Generated by Django 4.0.1 on 2022-01-30 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Name'),
        ),
    ]
