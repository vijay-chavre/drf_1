

from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Permission

class AccountSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    user_permissions = serializers.SerializerMethodField()
    class Meta:
        model = User
        exclude = ('password',)

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name
    def get_user_permissions(self, obj):
            # Retrieve the permissions assigned directly to the user and via groups
        user_permissions = obj.user_permissions.all()
        return user_permissions.values('id', 'name', 'codename')