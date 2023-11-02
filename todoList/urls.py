from django.urls import path
from . import views
urlpatterns = [
    path('tasks/', views.tasklist, name= "task_list"),
    
    path('taskdetail/<int:pk>', views.taskdetail, name='task_detail'),
    path('users/', views.userlist, name='userlist'),
]
