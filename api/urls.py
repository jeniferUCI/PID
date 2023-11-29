from django.urls import path, include
from .views import taskViews
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', taskViews, 'task')

urlpatterns = [
    path('', include(router.urls), name='TASK CRUD')
]