from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
