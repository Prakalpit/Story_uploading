from django.urls import path
from .views import index, Stories_form, dynamic_story
urlpatterns=[
    path('',index, name='index'),
    path('<int:id>/',dynamic_story, name='story'),
    path('upload/', Stories_form, name='form'),
]