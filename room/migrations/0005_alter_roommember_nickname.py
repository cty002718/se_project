# Generated by Django 3.2.2 on 2021-05-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_auto_20210523_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommember',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
    ]