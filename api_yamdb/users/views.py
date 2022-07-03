from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.permissions import AuthorizedOrReadOnly, UserOrAdminOrReadOnly
from users.models import User
from users.serializers import (SignUpSerializer, TokenSerializer,
                               UserSerializer, UsersSerializer)
from api_yamdb.settings import DENY_LIST


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (UserOrAdminOrReadOnly,)
    lookup_field = 'username'
    filter_backends = (SearchFilter, )

    @action(
        methods=('GET', 'PATCH'),
        detail=False,
        permission_classes=(AuthorizedOrReadOnly,),
        url_path=DENY_LIST)
    def get_current_user_info(self, request):
        if request.method != 'PATCH':
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        if request.user.is_admin or request.user.is_moderator:
            serializer = UsersSerializer(
                request.user,
                data=request.data,
                partial=True)
        else:
            serializer = UserSerializer(
                request.user,
                data=request.data,
                partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class APIGetToken(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = get_object_or_404(User, username=data['username'],)
        if data.get('confirmation_code') == user.confirmation_code:
            token = RefreshToken.for_user(user).access_token
            return Response({'token': str(token)},
                            status=status.HTTP_201_CREATED)
        return Response(
            {'неверный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST)


class APISignup(APIView):
    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def send_email(data):
        email = EmailMessage(
            body=data['mail_body'],
            to=[data['to_email']]
        )
        email.send()

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        mail_body = (
            f'{user.username}:'
            f'confirm_code: {user.confirmation_code}'
        )
        data = {
            'mail_body': mail_body,
            'to_email': user.email,
        }
        self.send_email(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
