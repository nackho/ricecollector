# Generated by Django 4.1.2 on 2022-10-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_dishes_dish_rename_ethnicity_dish_ethnicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='rice',
            name='dishes',
            field=models.ManyToManyField(to='main_app.dish'),
        ),
    ]
