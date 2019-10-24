from django.db import models
from django.urls import reverse


class Department(models.Model):

    department_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.department_name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})
