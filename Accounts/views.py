from rest_framework import viewsets
from .serializers import AccountSerializer
from .models import User
from drf_spectacular.utils import extend_schema

# Create your views here.
@extend_schema(summary="My Custom Endpoint", description="Detailed description of this API.")
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer