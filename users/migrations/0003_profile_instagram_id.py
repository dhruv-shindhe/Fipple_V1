# Generated by Django 3.1 on 2020-08-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200807_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram_ID',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
