# Generated by Django 4.2.7 on 2024-06-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
