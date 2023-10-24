from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

# Create your models here.


class User(AbstractUser):
    # create gender choices as a text choice field
    class Gender(models.TextChoices):
        male = "Male"
        female = "Female"

    """
    Default custom user model for Sts.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    first_name = models.CharField(_("First name"), max_length=30, blank=True)
    last_name = models.CharField(_("Last name"), max_length=150, blank=True)
    nickname = models.CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), max_length=30, unique=True)
    picture = models.ImageField(upload_to="profile_pictures/", default="profile_pictures/default.jpg")
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=30, blank=True)
    lives_in = models.CharField(max_length=30, blank=True)
    gender = models.CharField(
        max_length=30,
        blank=True,
        choices=Gender.choices,
        default=Gender.male,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
