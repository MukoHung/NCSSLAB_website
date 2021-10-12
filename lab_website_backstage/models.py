from django.db import models
from django.utils.translation import gettext_lazy as _

class MailRecipient(models.Model):
    email = models.EmailField(_('收件人'), max_length=254)

    def __str__(self):
        return self.email
