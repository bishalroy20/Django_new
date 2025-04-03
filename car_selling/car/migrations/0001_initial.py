# Generated by Django 5.1.5 on 2025-04-01 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='car/Images/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
    ]
