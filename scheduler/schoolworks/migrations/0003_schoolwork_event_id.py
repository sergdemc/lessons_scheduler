# Generated by Django 4.2.2 on 2023-07-02 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolworks', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolwork',
            name='event_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Event ID'),
        ),
    ]
