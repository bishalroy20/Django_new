# Generated by Django 5.1.5 on 2025-03-04 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtask',
            old_name='task_assign',
            new_name='task_assign_Date',
        ),
    ]
