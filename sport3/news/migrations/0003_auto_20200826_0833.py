# Generated by Django 3.1 on 2020-08-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200826_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynewsfb',
            name='content',
            field=models.TextField(),
        ),
    ]
