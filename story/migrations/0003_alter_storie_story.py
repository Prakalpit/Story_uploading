# Generated by Django 3.2.2 on 2021-05-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_rename_name_storie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storie',
            name='story',
            field=models.TextField(),
        ),
    ]