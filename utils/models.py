import json

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.
from utils.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, help_text=_('Required. 150 characters or fewer. '
                                                                           'Letters, digits and @/./+/-/_ only.'))
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    about_me = models.CharField(max_length=250, blank=True, null=True)

    def avatar_path(self, filename):
        return 'users/{0}/avatars/{1}'.format(self.id, filename)

    avatar = models.ImageField(upload_to=avatar_path, null=True, blank=True)

    def __str__(self):
        return self.email


class CustomUserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CustomUser):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Post(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    pub_date = models.DateTimeField(verbose_name="Дата публикации", default=datetime.datetime.now())
    text = models.TextField(null=True)

    def __str__(self):
        return self.name
