# Generated by Django 3.2.5 on 2021-09-06 05:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_website', '0006_auto_20210831_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObserReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='標題')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('last_edit_time', models.DateTimeField(auto_now=True, verbose_name='修改時間')),
                ('img', models.ImageField(upload_to='obser_report/images/', verbose_name='圖片')),
                ('file', models.FileField(blank=True, null=True, upload_to='obser_report/attachments/', verbose_name='附件')),
            ],
        ),
        migrations.CreateModel(
            name='TechReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='標題')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('last_edit_time', models.DateTimeField(auto_now=True, verbose_name='修改時間')),
                ('img', models.ImageField(upload_to='tech_report/images/', verbose_name='圖片')),
                ('file', models.FileField(blank=True, null=True, upload_to='tech_report/attachments/', verbose_name='附件')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='news/attachments/', verbose_name='附件'),
        ),
    ]
