from django.urls import path
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('<int:id>',views.profile,name='profile'),
    path('bio',views.user_bio,name='user_bio'),
    path('preference',views.Partner_preference,name='Partner_preference'),

    
]
