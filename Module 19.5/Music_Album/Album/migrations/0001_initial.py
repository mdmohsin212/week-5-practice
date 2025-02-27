# Generated by Django 5.1.1 on 2024-11-18 11:18

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_Name', models.CharField(max_length=30)),
                ('Date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('Rating', models.IntegerField(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5'), (1, '1')])),
                ('musicians', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicians.musicianmodel')),
            ],
        ),
    ]
