# Generated by Django 4.1 on 2022-09-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classic_app', '0002_alter_file_file_type_alter_file_upload_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
