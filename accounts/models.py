from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, city=None, street=None, phone=None, zips=None, state=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have an first name')
        if not last_name:
            raise ValueError('Users must have an last name')

        user = self.model(
            email       = self.normalize_email(email),
            first_name  = first_name,
            last_name   = last_name,
            city        = city,
            street      = street,
            phone       = phone,
            zips        = zips,
            state       = state,
            password    = password,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, city=None, street=None, phone=None, zips=None, state=None, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            first_name  = first_name,
            last_name   = last_name,
            city        = city,
            street      = street,
            phone       = phone,
            zips        = zips,
            state       = state,
            password    = password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_professionaluser(self, email, first_name, last_name, city=None, street=None, phone=None, zips=None, state=None, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            first_name  = first_name,
            last_name   = last_name,
            city        = city,
            street      = street,
            phone       = phone,
            zips        = zips,
            state       = state,
            password    = password,
        )
        user.professional = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, city=None, street=None, phone=None, zips=None, state=None, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            first_name  = first_name,
            last_name   = last_name,
            city        = city,
            street      = street,
            phone       = phone,
            zips        = zips,
            state       = state,
            password    = password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email   = models.EmailField(max_length=255,unique=True)
    active  = models.BooleanField(default=True)
    staff   = models.BooleanField(default=False) # a admin user; non super-user
    admin   = models.BooleanField(default=False) # a superuser
    first_name  = models.CharField(max_length=30,null=True,blank=False)
    last_name   = models.CharField(max_length=30,null=True,blank=False)
    professional = models.BooleanField(default=False)
    state       = models.CharField(max_length=30,null=True,blank=False)
    city        = models.CharField(max_length=30,null=True,blank=False)
    zips        = models.CharField(max_length=5,null=True,blank=False)
    street      = models.CharField(max_length=100,null=True,blank=False)
    phone       = models.CharField(max_length=12,null=True,blank=False)

    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name'] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        full_name = self.first_name + " " + self.last_name
        return full_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_professional(self):
        "Is the user a professional user"
        return self.professional

    @property
    def is_active(self):
        "Is the user active?"
        return self.active