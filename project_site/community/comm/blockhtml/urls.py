from . import views
from django.urls import include, path

app_name='blockhtml'
urlpatterns = [
    path('main/', views.main,name='main'),
    path('ora_list/', views.ora_list,name='ora_list'),
    path('notice_list/', views.notice_list,name='notice_list'),
    path('notice_read/', views.notice_read,name='notice_read'),
    
]
