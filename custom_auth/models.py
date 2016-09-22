import httplib2
from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone

from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import NotAcceptable


GENDER_CHOICES = (
    ('MA', 'Male'),
    ('FM', 'Female')
)

class UserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    full_name = models.CharField(_('full_name'), max_length=30, blank=True)
    mobile_number = models.CharField(_('mobile_number'), max_length=30, blank=True)
    default_billing_address = models.CharField(_('default_billing_address'), max_length=30, blank=True)
    default_shipping_address = models.CharField(_('default_shipping_address'), max_length=30, blank=True)
    mpesa_id = models.TextField(_('mpesa_id'), max_length=30, blank=True)
    is_admin = models.BooleanField(_('is_admin'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
