from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class News(models.Model):
    subject = models.CharField(_('標題'), max_length=200)
    content = RichTextField(_('內容'), blank=True, null=True)
    file = models.FileField(_('附件'), upload_to='news/attachments/', null=True, blank=True)
    date = models.DateTimeField(_('建立時間'), auto_now_add=True)
    last_edit_time = models.DateTimeField(_('修改時間'), auto_now=True)

    def __str__(self):
        return self.subject

class TechReport(models.Model):
    subject = models.CharField(_('標題'), max_length=200)
    content = RichTextField(_('內容'), blank=True, null=True)
    date = models.DateTimeField(_('建立時間'), auto_now_add=True)
    last_edit_time = models.DateTimeField(_('修改時間'), auto_now=True)
    img = models.ImageField(_('圖片'), upload_to='tech_report/images/')
    file = models.FileField(_('附件'), upload_to='tech_report/attachments/', null=True, blank=True)

    def __str__(self):
        return self.subject

class ObserReport(models.Model):
    subject = models.CharField(_('標題'), max_length=200)
    content = RichTextField(_('內容'), blank=True, null=True)
    date = models.DateTimeField(_('建立時間'), auto_now_add=True)
    last_edit_time = models.DateTimeField(_('修改時間'), auto_now=True)
    img = models.ImageField(_('圖片'), upload_to='obser_report/images/')
    file = models.FileField(_('附件'), upload_to='obser_report/attachments/', null=True, blank=True)

    def __str__(self):
        return self.subject