from django.urls import path
from . import views
urlpatterns = [

    path('info/', views.all_info,name="all_info"),
    path('python/', views.python,name="python"),
]
