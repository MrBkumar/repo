import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext as _
from config.models import ActivityTracking

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have a valid email address.")

        if not kwargs.get("username"):
            raise ValueError("Users must have a valid username.")

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get("username")
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account


class User(AbstractBaseUser, ActivityTracking, PermissionsMixin):

    GENDER_CHOICES = (("Male", "MALE"), ("Female", "FEMALE"))

    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(
        max_length=40, blank=True, null=True, default="", unique=True
    )
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    profile_image = models.ImageField(
        upload_to="profile_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Profile Image"),
    )
    description = models.CharField(max_length=255, blank=True)

    birth_date = models.CharField(max_length=10, default="", blank=True)
    address = models.CharField(max_length=255, default="", blank=True)
    phone = models.CharField(max_length=20, default="", blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=30, blank=True)
    pincode = models.CharField(max_length=8, blank=True)

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:users:user-list")


class UserCard(ActivityTracking):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="user_credit_card_detail"
    )
    card_number = models.CharField(max_length=19, blank=True, null=True)
    expiry_month_year = models.CharField(max_length=7, blank=True, null=True)
    stripe_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.card_number

    class Meta:
        verbose_name = "User Card Detail"
        verbose_name_plural = "User Card Details"
        ordering = ["-created_at"]