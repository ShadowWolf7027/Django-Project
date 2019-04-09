from django.db import models
from django.urls import reverse
from .file_reader import *

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    course = models.TextField(blank=True)

    def parse_file(self):
        return read

    @property
    def get_url(self):
        url = reverse('planner:event_view', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)