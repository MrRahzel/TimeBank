# Generated by Django 3.2.8 on 2022-03-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_usvers_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='usvers',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
