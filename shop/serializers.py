from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from shop.models import User, Shop, Category, ConfirmEmailToken
from rest_framework.exceptions import ValidationError, bad_request


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["password", "first_name", "last_name", "email", "type"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(**validated_data)

        return user


class ConfirmAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(max_length=150)


class LoginAccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=150)

    class Meta:
        model = ConfirmEmailToken
        fields = ['email', 'password']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'url')
        read_only_fields = ('id',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
        read_only_fields = ('id',)


# class StateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shop
#         fields = ('state')
