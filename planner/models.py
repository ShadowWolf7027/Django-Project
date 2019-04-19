from django.db import models
from django.urls import reverse
from .file_reader import *

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    course = models.TextField(blank=True)

    @property
    def parse_file(self):
        lessons = read()
        for lesson in lessons:
            for info in lesson:
                self.title = info[0]
                self.description = info[2] + info[3]
                self.start_time = info[1]
                self.end_time = info[1]
                self.course = 'MilArt'

    @property
    def get_url(self):
        url = reverse('planner:event_view', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)