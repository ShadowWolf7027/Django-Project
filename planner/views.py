from datetime import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse
import calendar

from .models import *
from .tools import Calendar
from .forms import EventForm

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
        m = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(m)
        context['next_month'] = next_month(m)        
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(m):
    first_day = m.replace(day=1)
    prev_month = first_day - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(m):
    month_days = calendar.monthrange(m.year, m.month)[1]
    last_day = m.replace(day = month_days)
    next_month = last_day + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('planner:planner'))
    return render(request, 'planner/event.html', {'form': form})

def fileStorage_view():
    pass