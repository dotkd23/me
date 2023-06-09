# Generated by Django 4.0.3 on 2023-04-09 02:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_carouselitem_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselitem',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='featureditem',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
