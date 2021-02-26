# Generated by Django 3.1.6 on 2021-02-26 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventspeaker',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=58),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventspeaker',
            name='what',
            field=models.CharField(default='ABCD ABCD ABCD ABCD ABCD ABCD\nABCD ABCD ABCD ABCD ABCD ABCD', max_length=58),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventspeaker',
            name='why',
            field=models.CharField(default='ABCD ABCD ABCD ABCD ABCD ABCD\nABCD ABCD ABCD ABCD ABCD ABCD', max_length=58),
            preserve_default=False,
        ),
    ]