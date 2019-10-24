from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .department import Department


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department = models.ForeignKey(
        Department, related_name="departments",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
# Every time a `User` is created, a matching `Employee`
# object will be created and attached as a one-to-one
# property
@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

# Every time a `User` is saved, its matching `Employee`
# object will be saved.
@receiver(post_save, sender=User)
def save_employee(sender, instance, **kwargs):
    instance.employee.save()
