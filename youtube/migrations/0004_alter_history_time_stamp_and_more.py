# Generated by Django 4.2.7 on 2023-11-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_user_vid_rel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='search_click',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_vid_rel',
            name='disliked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user_vid_rel',
            name='liked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]