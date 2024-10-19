from django.db import models

class User(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Сотрудники'
        ordering = ["id"]

    role = [
        ("admin", "Админ"),
        ("manager", "Менеджер"),
        ("client", "Клиент"),
    ]

    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Имя")
    surname = models.CharField(max_length=50, null=True, blank=True, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, null=True, blank=True, verbose_name="Отчество")
    job_title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Должность")
    phone = models.CharField(max_length=25, unique=True, null=True, blank=True, verbose_name="Номер телефона")
    tg_id = models.CharField(max_length=150, unique=True, null=True, blank=True, verbose_name="Телеграм ID")
    tg_chat_id = models.CharField(max_length=150, unique=True, null=True, blank=True, verbose_name="Чат ID")
    role = models.CharField(choices=role, default="client", verbose_name="Роль")

