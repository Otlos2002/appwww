# Generated by Django 5.1.2 on 2024-10-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]