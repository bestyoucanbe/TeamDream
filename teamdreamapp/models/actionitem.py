from django.db import models
from django.urls import reverse
from .sprint import Sprint
from .itemtype import ItemType


class ActionItem(models.Model):

    sprint = models.ForeignKey(
        Sprint, related_name="sprints",
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    itemtype = models.ForeignKey(
        ItemType, related_name="itemtypes",
        on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    start_date = models.DateField(null=True)
    finish_date = models.DateField(null=True)
    personal_benefit = models.CharField(max_length=50, blank=True, null=True)
    team_benefit = models.CharField(max_length=50, blank=True, null=True)
    presprint_review = models.BooleanField()

    class Meta:
        verbose_name = ("ActionItem")
        verbose_name_plural = ("ActionItems")

    def __str__(self):
        return f"Action Item Id: {self.pk} Description: {self.description} Associated Employee: {self.employee} Associated Sprint: {self.sprint} Associated Type: {self.itemtype}"

    def get_absolute_url(self):
        return reverse("ActionItem_detail", kwargs={"pk": self.pk})
