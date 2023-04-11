from django.db import models
from django.urls import reverse

from blog.models import Employee


class Visit(models.Model):
    employee: Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    visited = models.BooleanField(default=True)
    time_visit_start = models.TimeField()
    time_visit_end = models.TimeField()
    reason = models.CharField(max_length=255, blank=True)

    def get_abs_url(self):
        return reverse('detail_visit', kwargs={'id': self.id})

    def __str__(self):
        return f'{self.employee}'
