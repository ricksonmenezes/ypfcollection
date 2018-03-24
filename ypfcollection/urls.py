

from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from . import views

app_name = 'ypfcollection'
urlpatterns = [
      path('',views.index,name='index'),
	  path('create-match',views.create_match,name='create-match'),
	  path('collect-payments',views.collect_payments,name='collect-payments'),
      url(r'^ajax/get_credit/$', views.get_credit, name='get_credit'),
	  # path('<int:question_id>/results',views.results,name='results'),
	  # path('<int:question_id>/vote',views.vote,name='vote'),
	  ]