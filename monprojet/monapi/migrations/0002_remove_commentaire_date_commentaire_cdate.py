# Generated by Django 4.1.7 on 2023-03-09 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='date',
        ),
        migrations.AddField(
            model_name='commentaire',
            name='cdate',
            field=models.DateField(null=True),
        ),
    ]
