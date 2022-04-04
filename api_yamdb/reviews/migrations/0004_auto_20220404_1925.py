# Generated by Django 2.2.16 on 2022-04-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_comment_title_id'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title_id', 'author'), name='unique_title_review'),
        ),
    ]
