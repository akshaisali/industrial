# Generated by Django 4.0.6 on 2024-07-30 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_remove_materialdetail_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialdetail',
            name='is_heading',
            field=models.BooleanField(default=False),
        ),
    ]