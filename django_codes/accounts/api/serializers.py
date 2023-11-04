from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "id")


class UserTokenSerializer(serializers.ModelSerializer):
    refresh = serializers.CharField()
    access = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "refresh",
            "access",
            "username",
            "email",
            "id",
        )


class UserObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_serializer = UserProfileSerializer(self.user)
        data.update(user_serializer.data)
        return data
