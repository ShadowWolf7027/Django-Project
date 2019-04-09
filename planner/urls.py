from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'planner'
urlpatterns = [
    url(r'^planner/$', views.PlannerView.as_view(), name='planner'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    url(r'^event/view/(?P<event_id>\d+)/$', views.eventview, name='event_view'),
]