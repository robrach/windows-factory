# Generated by Django 4.1.1 on 2022-09-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_alter_window_additional_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
