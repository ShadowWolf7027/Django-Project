from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_url(self):
        url = reverse('planner:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Month(models.Model):
    prev_month = models.CharField(max_length=200)
    next_month = models.CharField(max_length=200)
    event = models.CharField(max_length=200)
    pass

class FileStorage(models.Model):
    upload = models.FileField()
    pass