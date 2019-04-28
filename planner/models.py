from django.db import models
from django.urls import reverse
from .file_reader import *
import datetime
import django.utils
import datefinder

class Event(models.Model):
    title = models.CharField(max_length=200, blank = True)
    description = models.TextField(blank=True)
    date = models.DateField(null=True,blank=True)
    course = models.TextField(blank=True)

    def save(self):
        lessons = read()
        bulk_lessons = []
        for lesson in lessons:
            new_lesson = Event()
            new_lesson.title = str(lesson[0])
            new_lesson.description = str(lesson[2] + lesson[3])
            l = datefinder.find_dates(str(lesson[1]))
            for d in l:
                new_lesson.date = d.date()
                self.date = d.date()
            new_lesson.course = 'MilArt'
            bulk_lessons.append(new_lesson)
        Event.objects.bulk_create(bulk_lessons)

    @property
    def get_url(self):
        url = reverse('planner:event_view', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)