# Generated by Django 3.0.5 on 2020-04-11 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eadlogin', '0003_remove_login_info_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login_info',
        ),
    ]
