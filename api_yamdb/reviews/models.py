from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import six

class User(AbstractUser):
    ADMIN = 'A'
    MODERATOR = 'M'
    USER = 'U'
    USER_ROLES = (
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user'),
    )
    role = models.CharField(
        max_length=1, 
        choices=USER_ROLES, 
        default=USER
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория',
        max_length=256
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=256
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    year = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(verbose_name='Описание')
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Slug жанра'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Slug категории'
    )

    def __str__(self):
        return self.name
