# Generated by Django 3.1.3 on 2020-12-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_requirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='food_category',
            field=models.TextField(),
        ),
    ]
