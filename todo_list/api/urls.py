from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'api/task', views.TaskApiView, basename='task')

urlpatterns = router.urls

urlpatterns += [

]
