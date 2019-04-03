from datetime import timedelta, datetime, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse
import calendar

from .models import Event
from .tools import Calendar
from .forms import EventForm

class PlannerView(generic.ListView):
    model = Event
    template_name = 'planner/planner.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        plan = Calendar(d.year, d.month)
        html_plan = plan.formatmonth(withyear=True)
        context['planner'] = mark_safe(html_plan)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    month_days = calendar.monthrange(d.year, d.month)[1]
    last_day = d.replace(day = month_days)
    n_month = last_day + timedelta(days=1)
    month = 'month=' + str(n_month.year) + '-' + str(n_month.month)
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