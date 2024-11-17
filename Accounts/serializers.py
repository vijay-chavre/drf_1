

from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Permission
import re
from django.core.exceptions import ValidationError

class AccountSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    user_permissions = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'full_name', 'user_permissions', 'password']
    
    def validate_empty_values(self, data):
        return super().validate_empty_values(data)
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Za-z]', value):
            raise serializers.ValidationError("Password must contain at least one letter.")
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("Password must contain at least one number.")
        if not re.search(r'[@$!%*?&]', value):
            raise serializers.ValidationError("Password must contain at least one special character (@$!%*?&).")
        return value
       
    def create(self, validated_data):
        print(validated_data)
        password = self.context['request'].data.get('password')
        if not password:
            raise serializers.ValidationError({'password': 'Password is required'})
        user = User.objects.create(**validated_data)
        user.set_password(password)  # Make sure to hash the password before saving
        user.save()
        return user

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name
    def get_user_permissions(self, obj):
            # Retrieve the permissions assigned directly to the user and via groups
        user_permissions = obj.user_permissions.all()
        return user_permissions.values('id', 'name', 'codename')