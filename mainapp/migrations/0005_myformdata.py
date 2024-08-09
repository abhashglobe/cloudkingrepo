# Generated by Django 5.0.6 on 2024-08-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]
