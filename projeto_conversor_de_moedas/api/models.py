from django.db import models
from django.urls import reverse


class Conversor(models.Model):

    class Meta:
        verbose_name = "Conversor"
        verbose_name_plural = "Conversores"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Conversor_detail", kwargs={"pk": self.pk})
