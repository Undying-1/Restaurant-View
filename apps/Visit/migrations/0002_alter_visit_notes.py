# Generated by Django 5.0.1 on 2024-01-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]