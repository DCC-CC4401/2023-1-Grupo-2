# Generated by Django 4.2 on 2023-04-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='budget',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='budget',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='display_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
