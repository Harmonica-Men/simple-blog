# Generated by Django 4.2.7 on 2024-06-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0003_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='title blog', max_length=200),
        ),
    ]
