# Generated by Django 3.2.5 on 2021-08-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20210818_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
