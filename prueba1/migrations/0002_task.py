# Generated by Django 4.1.5 on 2023-01-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
