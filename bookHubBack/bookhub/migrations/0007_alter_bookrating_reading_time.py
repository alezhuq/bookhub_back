# Generated by Django 4.2 on 2024-06-01 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookhub', '0006_alter_bookrating_comment_alter_bookrating_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrating',
            name='reading_time',
            field=models.DurationField(blank=True, default=datetime.timedelta(0), null=True),
        ),
    ]
