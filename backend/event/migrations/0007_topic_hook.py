# Generated by Django 3.1.6 on 2021-02-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20210226_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='hook',
            field=models.CharField(default='a', max_length=69),
            preserve_default=False,
        ),
    ]
