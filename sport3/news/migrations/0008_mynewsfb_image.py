# Generated by Django 3.1 on 2020-09-04 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_mynewsfb_time_created_varzesh3'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynewsfb',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='news_pics'),
        ),
    ]
