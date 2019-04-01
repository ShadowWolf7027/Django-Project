from django.conf.urls import url
from . import views

app_name = 'planner'
urlpatterns = [
    # url(r'^index/$', views.index, name='index'),
    # url(r'^planner/$', views.PlannerView.as_view(), name='planner')
    url(r'', views.PlannerView.as_view(), name='planner'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),

]