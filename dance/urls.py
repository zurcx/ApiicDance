# encoding: utf-8


from django.conf.urls import patterns, include, url

from .views import DanceStepView, DanceStepListView

urlpatterns = patterns('',
    url(r'^categoria/(?P<slug>[\w_-]+)/', DanceStepListView.as_view(),
        name='dancestep_by_rhythm'),
    url(r'^passos/(?P<slug>[\w_-]+)/', DanceStepView.as_view(),
        name='dancestep_details'),

)