# Generated by Django 3.2.2 on 2021-05-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210526_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(default=123, max_length=30),
            preserve_default=False,
        ),
    ]