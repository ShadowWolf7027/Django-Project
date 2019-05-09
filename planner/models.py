from django.db import models
from django.urls import reverse
from .file_reader import read
import datetime
import django.utils
import datefinder

class Event(models.Model):
    title = models.CharField(max_length=200, blank = True)
    description = models.TextField(blank=True)
    date = models.DateField(null=True,blank=True)
    course = models.TextField(blank=True)
    
    # Override the save function to allow input saves and auto-generation 
    # of model instances
    def save(self):
        if (not self.title or not self.description or
            not self.date or not self.course):
            lessons = read()
            bulk_lessons = []
            for lesson in lessons:
                new_lesson = Event()
                new_lesson.title = 'MilArt ' + ' '.join(lesson[0])
                new_lesson.description = ' '.join(lesson[2] + lesson[3])
                l = datefinder.find_dates(' '.join(lesson[1]))
                for d in l:
                    new_lesson.date = d.date()
                    self.date = d.date()
                new_lesson.course = 'MilArt'
                bulk_lessons.append(new_lesson)
            Event.objects.bulk_create(bulk_lessons)
        else:
            super(Event, self).save()

    # Allow a user to click in an event and see it's details in a separate page
    @property
    def get_url(self):
        url = reverse('planner:event_view', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)