from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import validate_username

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'


class User(AbstractUser):
    ROLES = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )
    username = models.CharField(
        validators=(validate_username,),
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Username',
        help_text='Введите username.'
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Почта',
        help_text='Введите email.'
    )
    role = models.CharField(
        max_length=30,
        choices=ROLES,
        default=USER,
        blank=True,
        verbose_name='Роль',
        help_text='Выберите роль пользователя.'
    )
    confirmation_code = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        default='def_confirm_code',
        verbose_name='Код подтверждения',
        help_text='Введите код подтверждения.'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='О себе',
        help_text='Введите текст.'
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Имя',
        help_text='Введите имя.'
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Фамилия',
        help_text='Введите фамилия.'
    )

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    def __str__(self):
        return self.username
