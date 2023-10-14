from rest_framework import serializers
from .models import Rating
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
    )
    class Meta:
        model = Rating
        fields = ['user', 'menuitem_id', 'rating']
        validators = [UniqueTogetherValidator(queryset=Rating.objects.all(), fields=['user', 'menuitem_id'])]
        extra_kwargs = {
            'rating': {
                'max_value': 5,
                'min_value': 0,
            }
        }

# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'first_name', 'last_name', 'phone')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True},
#         }
        
#     def validate_password(self, value):
#         # Use Django's password validation to ensure a strong password
#         validate_password(value)
#         return value