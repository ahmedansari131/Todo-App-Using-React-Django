# Generated by Django 4.2.6 on 2023-11-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_todolist_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='color',
            field=models.CharField(default='', max_length=10),
        ),
    ]
