# Generated by Django 4.1.2 on 2022-10-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=100)),
                ('usage', models.TextField(max_length=250)),
            ],
        ),
    ]