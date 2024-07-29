from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class ProfileManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Profile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    role_choices_type = [
        ('Principal', 'Principal'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]
    role = models.CharField(max_length=10, choices=role_choices_type)
    password = models.CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number', 'role']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='profile_user_set',  # Unique related_name for groups
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='profile_user_set',  # Unique related_name for user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email


class Organization(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=350)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    phone_no = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    gst_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name
