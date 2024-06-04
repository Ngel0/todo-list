from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views

router = routers.DefaultRouter()
router.register(r'api/tasklists', views.TaskListApiView, basename='tasklist')
router.register(r'api/tasks', views.TaskApiView, basename='task')

urlpatterns = router.urls

urlpatterns += [
    # Get tasks for a specific tasklist by ID
    path('api/tasklists/<int:pk>/tasks/', views.TaskListTasksApiView.as_view(), name='tasklist-tasks'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api-token-auth/', obtain_auth_token),
]
