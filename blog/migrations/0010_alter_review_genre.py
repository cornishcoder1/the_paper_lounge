# Generated by Django 3.2.13 on 2022-05-30 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_review_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.genre'),
        ),
    ]