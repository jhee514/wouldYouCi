from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from drf_yasg import openapi


class UserMessageField(serializers.JSONField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "title": "User",
            "properties": {
                "username": openapi.Schema(
                    title="username",
                    type=openapi.TYPE_STRING,
                ),
                "email": openapi.Schema(
                    title="email",
                    type=openapi.TYPE_STRING,
                ),
            },
            "required": ["username", "email"],
         }


class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'get_agreement', 'email')

    message = UserMessageField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
