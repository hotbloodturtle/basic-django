# Generated by Django 3.0.8 on 2020-10-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_board_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
