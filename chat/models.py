from django.db import models

from django.conf import settings
from django.db import models
from django.db.models import Q


class ThreadManager(models.Manager):
    def by_user(self, user):
        qlookup = Q(first=user) | Q(second=user)
        qlookup2 = Q(first=user) & Q(second=user)
        qs = self.get_queryset().filter(qlookup).exclude(qlookup2).distinct()
        return qs

    def get_or_new(self, user, other_username):  # get_or_create
        username = user.email
        if username == other_username:
            return None
        qlookup1 = Q(first__email=username) & Q(second__email=other_username)
        qlookup2 = Q(first__email=other_username) & Q(second__email=username)
        qs = self.get_queryset().filter(qlookup1 | qlookup2).distinct()
        if qs.count() == 1:
            return qs.first(), False
        elif qs.count() > 1:
            return qs.order_by('timestamp').first(), False
        else:
            Klass = user.__class__
            user2 = Klass.objects.get(email=other_username)
            if user != user2:
                obj = self.model(
                    first=user,
                    second=user2
                )
                obj.save()
                return obj, True
            return None, False


class Thread(models.Model):
    first = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_thread_first',
                              verbose_name='Первый')
    second = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_thread_second',
                               verbose_name='Второй')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата')
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()

    @property
    def room_group_name(self):
        return f'chat_{self.id}'

    def broadcast(self, msg=None):
        if msg is not None:
            broadcast_msg_to_chat(msg, group_name=self.room_group_name, user='admin')
            return True
        return False

    class Meta:
        verbose_name = 'Переписка'
        verbose_name_plural = 'Переписки'

    def __str__(self):
        return '{} {}'.format(self.first, self.second)


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.SET_NULL, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Отправитель', on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Сообщение')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Переписка'
        verbose_name_plural = 'Переписки'
