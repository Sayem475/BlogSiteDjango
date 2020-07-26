# Generated by Django 3.0.6 on 2020-07-05 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_design_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='htmlchapters',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('chapter_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='htmldescription',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('chapters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.htmlchapters')),
            ],
        ),
    ]
