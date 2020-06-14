from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('Должно быть введено имя пользователя.')
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('У суперпользователя поле is_superuser должен быть True.')
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=30, blank=False, unique=True,
                                verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, blank=False, verbose_name='Почта')
    password = models.CharField(max_length=128, blank=False, null=False, verbose_name='Пароль')
    first_name = models.CharField(max_length=30, blank=False, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=False, null=False, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='profile-photo/', blank=True, null=True, verbose_name='Фотография')
    phone = models.CharField(max_length=30, blank=False, null=False, verbose_name='Телефон')
    is_active = models.BooleanField(default=False, verbose_name='Активный')
    is_client = models.BooleanField(default=False, verbose_name='Клиент')
    is_consultant = models.BooleanField(default=False, verbose_name='Исполнитель')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
