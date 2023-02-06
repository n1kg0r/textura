# Generated by Django 4.1.2 on 2022-11-13 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textura_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedtext',
            name='avg_sentence_length_stdev',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='uploadedtext',
            name='max_sentence_length',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='uploadedtext',
            name='max_word_length',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedtext',
            name='avg_sentence_length',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedtext',
            name='file',
            field=models.FileField(upload_to='texts/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt'])]),
        ),
    ]