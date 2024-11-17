from rest_framework import viewsets
from .serializers import AccountSerializer
from rest_framework import permissions
from .models import User
from drf_spectacular.utils import extend_schema

from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.action == 'create':
            return []
        return [IsAuthenticated()]

class ListUsersView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = AccountSerializer