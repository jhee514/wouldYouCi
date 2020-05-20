from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'get_agreement', 'email')




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
