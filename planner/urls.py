from django.conf.urls import url
from . import views

app_name = 'planner'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^planner/$', views.PlannerView.as_view(), name='planner')
]