from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('login_view/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('plan/', views.plan, name='plan'),
    path('update_task_status/', views.update_task_status, name='update_task_status'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('add_view', views.add_view, name='add_view')
]