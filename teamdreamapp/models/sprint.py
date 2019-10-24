from django.db import models
from django.urls import reverse


class Sprint(models.Model):

    sprint_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = ("Sprint")
        verbose_name_plural = ("Sprints")

    def __str__(self):
        return self.sprint_name

    def get_absolute_url(self):
        return reverse("Sprint_detail", kwargs={"pk": self.pk})
