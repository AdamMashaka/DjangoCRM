# Generated by Django 5.1.3 on 2024-11-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='language_code',
            field=models.CharField(blank=True, choices=[('en', 'English')], default='', max_length=7, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='language_code',
            field=models.CharField(choices=[('en', 'English')], max_length=7, verbose_name='Language'),
        ),
    ]