# Generated by Django 3.0.5 on 2020-04-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_info',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
