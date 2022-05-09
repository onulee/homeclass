from . import views
from django.urls import path

app_name='stboard'
urlpatterns = [
    path('tpage/',views.tpage,name='tpage'),
    path('tpage2/',views.tpage2,name='tpage2'),
]
