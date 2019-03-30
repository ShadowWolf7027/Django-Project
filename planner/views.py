from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .tools import Calendar

def index(request):
    return HttpResponse('hello')

class PlannerView(generic.ListView):
    model = Event
    template_name = 'planner/planner.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = get_date(self.request.GET.get('day', None))
        planner = Calendar(date.year, date.month)
        planner_html = planner.formatmonth(withyear=True)
        context['planner'] = mark_safe(planner_html)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def months_view():
    pass

def days_view():
    pass

def events_view():
    pass

def fileStorage_view():
    pass