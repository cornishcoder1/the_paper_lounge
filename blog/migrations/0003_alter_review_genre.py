# Generated by Django 3.2.13 on 2022-05-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220527_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]