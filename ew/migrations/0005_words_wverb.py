# Generated by Django 3.0.7 on 2021-09-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ew', '0004_examples_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='wverb',
            field=models.BooleanField(default=True, verbose_name='動詞かどうか'),
        ),
    ]
