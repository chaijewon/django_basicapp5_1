from django.urls import path
from .views import *
'''
   path('')   /notice/
   path('add/') /notice/add/
   path('delete/') /notice/delete/
'''
urlpatterns=[
    path('',NoticeListView.as_view(),name='list'),
    path('detail/<int:pk>',NoticeDetailView.as_view(),name='detail'),
    path('update/<int:pk>',NoticeUpdateView.as_view(),name='update'),
]