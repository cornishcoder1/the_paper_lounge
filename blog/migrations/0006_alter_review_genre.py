# Generated by Django 3.2.13 on 2022-05-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_review_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.IntegerField(blank=True, choices=[(0, '--------'), (1, 'Crime'), (2, 'Romance')], null=True),
        ),
    ]
