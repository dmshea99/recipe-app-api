"""
Database models
"""
from django.conf import settings  # noqa
from django.db import models  # noqa
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin)


class UserManager(BaseUserManager):
    """Manager for Users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("an email must be supplied!")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Recipe(models.Model):
    """Recipe object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField('Tag')
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.title


class Quote(models.Model):
    """Quote object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    tag_choices = [('Inspirational', 'Inspirational'),
                   ('Political', 'Political'),
                   ('Cynical', 'Cynical'),
                   ('Dark', 'Dark'),
                   ('Comical', 'Comical'),
                   ('Literary', 'Literary'),
                   ('Friends', 'Friends'),
                   ('Love', 'Love'),
                   ('Wisdom', 'Wisdom'),
                   ('Poetry', 'Poetry'),
                   ('Health', 'Health',)

                   ]
    author = models.CharField(max_length=255)
    text = models.TextField(blank=False)
    link = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    tag1 = models.CharField(max_length=50, choices=tag_choices, blank=True)
    tag2 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Quote from {self.author}: {self.text[:20]}"


class Tag(models.Model):
    """Tag for filtering recipes."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient for recipes."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
