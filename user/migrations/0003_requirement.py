# Generated by Django 3.1.3 on 2020-12-21 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20201220_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('times', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('food', models.CharField(max_length=10)),
                ('food_category', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
