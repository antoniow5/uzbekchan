from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#from .managers import UserManager


class Category(models.Model):
    name = models.CharField(max_length=20)
    order = models.PositiveSmallIntegerField()

class Board(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    prefix = models.SlugField(max_length=6, unique = True)
    name = models.CharField(max_length=20)
    is_userboard = models.BooleanField(default = False)
    thread_limit = models.PositiveSmallIntegerField()
    banner = models.FileField(null = True, blank=True)
    order = models.PositiveSmallIntegerField()
    is_adult = models.BooleanField(default = False)
    anon_can_post = models.BooleanField(default = True)
    show_on_main = models.BooleanField(default = True)
    is_deprecated = models.BooleanField(default = False)
    bump_limit = models.PositiveIntegerField()
    max_threads = models.PositiveIntegerField()
    default_name = models.CharField(max_length=20, default = "Аноним")
    enable_dices = models.BooleanField(default=False)
    enable_flags = models.BooleanField(default = False)
    enable_likes = models.BooleanField(default = False)
    enable_names = models.BooleanField(default = False)
    enable_oekaki = models.BooleanField(default = False)
    enable_sage = models.BooleanField(default = True)
    enable_subject = models.BooleanField(default = True)
    enable_thread_tags = models.BooleanField(default = False)
    is_protected = models.BooleanField(default = False)

class Tag(models.Model):
    border = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    order = models.PositiveSmallIntegerField()
    prefix = models.SlugField(max_length=6, unique = True)

class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete = models.CASCADE, related_name='threads')
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null = True, blank = True)
    is_pinned = models.BooleanField(default = False)
    is_locked = models.BooleanField(default = False) 
    date = models.DateTimeField(default=timezone.now)

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts',default=1)
    subject = models.CharField(max_length=100)
    text = models.CharField(max_length= 5000)
    number = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)

class Attachment(models.Model):
    pass
        
class ApplicationUser(AbstractBaseUser, PermissionsMixin) :
    user_session_id = models.CharField(max_length=128)
    user_settings_json = models.CharField(max_length=10000)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="applicationuser_set",
        related_query_name="applicationuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="applicationuser_set",
        related_query_name="applicationuser",
    )


