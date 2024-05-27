from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'required': True},'email': {'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer to include user details

    class Meta:
        model = Profile
        fields = ['user','pk',  'fname', 'lname', 'photo', 'bdate', 'gender'
                  , 'city', 'home_address', 'phone']


class ProviderProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer to include user details

    class Meta:
        model = Profile
        fields = ['user','pk',  'fname', 'lname', 'photo', 'bdate', 'gender'
                  , 'city', 'home_address', 'phone', 'is_craftsman', 
                  'service', 'description', 'work_from',
                  'work_to', 'price_from', 'price_to', 'work_address']

class PersonalInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer to include user details

    class Meta:
        model = Profile
        fields = ['user', 'pk', 'fname', 'lname', 'photo', 'bdate', 'gender'
                  , 'city', 'home_address', 'phone', 'is_craftsman']


class WorkInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer to include user details
    class Meta:
        model = Profile
        fields = ['user', 'pk','service', 'description', 'work_from',
                  'work_to', 'price_from', 'price_to', 'work_address']
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)


class ChangeEmailSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    new_email = serializers.EmailField(required=True)

    def validate_new_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
    

class DeleteUserSerializer(serializers.ModelSerializer):
    confirm = serializers.BooleanField()

    class Meta:
        model = User
        fields = ['id', 'confirm']

    def validate_confirm(self, value):
        if value != True:
            raise serializers.ValidationError("You must confirm the deletion.")
        return value