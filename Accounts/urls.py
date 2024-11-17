

from .views import UserViewSet, ListUsersView
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = [
   path('', include(router.urls)),
   path('list/', ListUsersView.as_view({'get': 'list'}), name='list-users'),
]
