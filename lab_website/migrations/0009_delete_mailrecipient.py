# Generated by Django 3.2.5 on 2021-09-19 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_website', '0008_mailrecipient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MailRecipient',
        ),
    ]