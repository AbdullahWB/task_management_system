# Generated by Django 4.2.13 on 2024-08-03 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskcategory',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='taskcategory',
            name='tasks',
        ),
    ]
