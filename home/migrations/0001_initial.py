# Generated by Django 3.0.6 on 2020-06-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=30)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
