# Generated by Django 3.1.3 on 2023-07-08 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20230708_0159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_id',
            new_name='question',
        ),
    ]
