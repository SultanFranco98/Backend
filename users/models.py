from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.safestring import mark_safe


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, **extra_fields):
        if email:
            email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, blank=False, verbose_name='Почта')
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

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Consultant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    comment = models.TextField(max_length=200, blank=True, null=True, verbose_name='Комментарии')

    class Meta:
        verbose_name = 'Консультант'
        verbose_name_plural = 'Консультанты'

    def __str__(self):
        return '{}'.format(self.user)

    def short_description(self):
        return truncatechars(self.description, 270)

    short_description.short_description = 'О себе'


class Specialty(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Специальность')

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

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

    def get_certificate(self):
        return self.certificate_image.url

    def certificate_tag(self):
        return mark_safe('<img src="%s" />' % self.get_certificate())

    certificate_tag.short_description = 'Сертификаты'


class CategoryConsultant(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name='specialty', verbose_name='Консультант')
    category = models.ForeignKey(Specialty, on_delete=models.CASCADE, blank=False, null=False,
                                 verbose_name='Специальность')

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
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, verbose_name='Консультант',
                                   related_name="ratings")
    star = models.ForeignKey(RatingStart, on_delete=models.CASCADE, verbose_name='Звезда')

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField()
    text = models.TextField(max_length=5000, verbose_name='Сообщение')
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, verbose_name='Консультант',
                                   related_name='reviews')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
