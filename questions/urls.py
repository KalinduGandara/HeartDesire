from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('',views.questionD,name='questionD'),
    path('<int:q>/',views.question,name='question')
]
