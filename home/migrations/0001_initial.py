# Generated by Django 3.2.6 on 2021-08-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('comment', models.TextField(max_length=122)),
                ('city', models.TextField(max_length=122)),
                ('subject', models.TextField(max_length=122)),
                ('date', models.DateField()),
                ('che', models.BooleanField()),
            ],
        ),
    ]