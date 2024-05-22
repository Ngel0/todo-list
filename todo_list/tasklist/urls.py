from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskItemList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskItemDetail.as_view(), name='task'),
    path('create-task/', views.TaskItemCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', views.TaskItemUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', views.TaskItemDelete.as_view(), name='delete-task'),
    path('tasklists/', views.TaskListList.as_view(), name='tasklists'),
    path('tasklist/<int:pk>/', views.TaskListDetail.as_view(), name='tasklist-detail'),
    path('create-tasklist/', views.TaskListCreate.as_view(), name='create-tasklist'),
    path('update-tasklist/<int:pk>/', views.TaskListUpdate.as_view(), name='update-tasklist'),
    path('delete-tasklist/<int:pk>/', views.TaskListDelete.as_view(), name='delete-tasklist'),
    path('accounts/', include('accounts.urls')),
]
