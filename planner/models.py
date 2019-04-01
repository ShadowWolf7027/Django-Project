from django.db import models
from django.urls import reverse

class Calendar(models.Model):
    pass

class Months(models.Model):
    pass

class Days(models.Model):
    pass

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_url(self):
        url = reverse('planner:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class FileStorage(models.Model):
    pass