# Generated by Django 5.1.2 on 2024-10-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pbx_number',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Phone'),
        ),
    ]