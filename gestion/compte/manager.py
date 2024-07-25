

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, username, email, password, *args, **kwargs):

        if not email:

            raise ValueError(_('The email address must bet set'))
        
        email = self.normalize_email(email)

        user = self.model(email=email, username=username, *args, **kwargs)

        user.set_password(password)

        user.save()

        return user


        # *********************
    
    def create_superuser(self, username, email, password, **extra_fields):
        # create and save super user
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)
