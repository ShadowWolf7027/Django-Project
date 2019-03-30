from django.db import models

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

class FileStorage(models.Model):
    pass