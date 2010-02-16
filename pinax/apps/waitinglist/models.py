from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _



class WaitingListEntry(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(default=datetime.now, editable=False)
    
    class Meta:
        verbose_name = _("waiting list entry")
        verbose_name_plural = _("waiting list entries")
