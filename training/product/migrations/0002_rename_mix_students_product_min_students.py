# Generated by Django 4.2 on 2024-03-01 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='mix_students',
            new_name='min_students',
        ),
    ]