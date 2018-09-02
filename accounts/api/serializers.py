from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
)

User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_email(self, value):
        data = self.get_initial()
        email1 = value
        email2 = data['email2']

        user_obj = User.objects.filter(email=email1)

        if email1 != email2:
            raise ValidationError('Emails must match.')

        if user_obj.exists():
            raise ValidationError('The email already registered.')

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data['email']
        email2 = value

        if email1 != email2:
            raise ValidationError('Emails must match')

        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username=username,
            email=email
        )

        user_obj.set_password(password)
        user_obj.save()

        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, data):
        user_obj = None
        username = data.get('username', None)
        email = data.get('email', None)
        password = data['password']

        if not username and not email:
            raise ValidationError('A username or email is required to login.')

        user = User.objects.filter(
            Q(username=username) |
            Q(email=email)
        ).distinct()

        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        # print(user)

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('The username or email is not valid.')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect credentials.')

        data['token'] = 'Some Random Token'

        return data
