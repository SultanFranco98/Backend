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


class Consultant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    description = models.TextField(blank=False, null=False, verbose_name='Описание')
    comment = models.TextField(max_length=200, blank=True, null=True, verbose_name='Комментарии')

    class Meta:
        verbose_name = 'Консультант'
        verbose_name_plural = 'Консультанты'

    def __str__(self):
        return '{}'.format(self.user)


class Category(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class ImageConsultant(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name='certificates',
                                   verbose_name='Консультант')
    certificate_image = models.ImageField(upload_to='certificate-image/', blank=True, null=True,
                                          verbose_name='Сертификаты')

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return '{}'.format(self.consultant)


class CategoryConsultant(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name='specialty', verbose_name='Консультант')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Категории')

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return '{}'.format(self.consultant)


class RatingStart(models.Model):
    value = models.SmallIntegerField(default=0, verbose_name='Значение')

    def __str__(self):
        return '{}'.format(self.value)

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, verbose_name='Консультант', related_name="ratings")
    star = models.ForeignKey(RatingStart, on_delete=models.CASCADE, verbose_name='Звезда')

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
