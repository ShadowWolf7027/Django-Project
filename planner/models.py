from django.db import models
from django.urls import reverse
from .file_reader import *
import datetime
import django.utils
import datefinder

class Event(models.Model):
    title = models.CharField(max_length=200, blank = True)
    description = models.TextField(blank=True)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    date = models.DateField(blank=True)#default=datetime.date.today(), blank=True)
    course = models.TextField(blank=True)

    def save(self):
        lessons = read()
        for lesson in lessons:
            # for info in lesson:
            self.title = str(lesson[0])
            self.description = str(lesson[2] + lesson[3])
            # self.start_time = str(lesson[1])
            # self.end_time = str(lesson[1])
            l = datefinder.find_dates(str(lesson[1]))
            for d in l:
                self.date = d.date()
            self.course = 'MilArt'
        super(Event, self).save()

    @property
    def get_url(self):
        url = reverse('planner:event_view', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)