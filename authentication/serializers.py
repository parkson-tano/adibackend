from rest_framework import serializers
# from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['admin'] = user.admin
        return token 

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'phone_number',
                  'first_name', 'last_name', 'date_created', 
                   'country', 'town', 'quater', 'address', 'admin')
                    


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                     message='This email is already taken')]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'email', 'first_name',
                  'last_name', 'phone_number', 'country', 'town', 'quater', 'address', 'admin')
        extra_kwargs = {
            'last_name': {'required': False}
        }


    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            country=validated_data['country'],
            town=validated_data['town'],
            quater=validated_data['quater'],
            address=validated_data['address'],
            admin = validated_data['admin'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)