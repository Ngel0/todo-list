from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r'api/tasklist', views.TaskListApiView, basename='tasklist')
router.register(r'api/task', views.TaskApiView, basename='task')

urlpatterns = router.urls

urlpatterns += [
    path('api-token-auth/', obtain_auth_token),
]
