# Generated by Django 3.0.6 on 2020-06-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20200623_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
