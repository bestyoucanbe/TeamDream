from django.db import models
from django.urls import reverse


class ItemType(models.Model):

    action_desc = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("ItemType")
        verbose_name_plural = ("ItemTypes")

    def __str__(self):
        return self.action_desc

    def get_absolute_url(self):
        return reverse("ItemType_detail", kwargs={"pk": self.pk})
