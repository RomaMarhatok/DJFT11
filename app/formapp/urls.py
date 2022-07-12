from django.urls import path
from .views import index,models_list
urlpatterns = [
    path('index/',index,name="index"),
    path('all/',models_list,name="all")
]