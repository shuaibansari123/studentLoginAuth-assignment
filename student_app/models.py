from django.db import models

# Create your models here.
from django.contrib.auth.models import UserManager , PermissionsMixin  , AbstractBaseUser

# assuming student is user
import datetime


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        #extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        #extra_fields.setdefault("is_active", True)
        print(extra_fields)

        # if extra_fields.get("is_staff") is not True:
        #     raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class Student(AbstractBaseUser , PermissionsMixin):
    # we can use builtin choices fields

    student_types_choices = (('junior', 'junior') , 
                    ('senior' , 'senior') ,
                    ('staff' , 'staff') , 
                    ('worker' , 'worker')
                    )

    email = models.EmailField( unique=True) # we can validate emails formats
    username = models.CharField(max_length= 255, blank=False , null=False)
    student_class = models.IntegerField(null=True , blank=True) # we can use choices


    student_type = models.CharField(choices=student_types_choices , max_length = 100 , default='junior')
    joining_date = models.DateTimeField(null=True , blank=True) # assuming user will select
    date_of_birth = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [] 

    @property
    def age(self):
        print(datetime.datetime.year , self.date_of_birth.year )
        today = datetime.date.today()
        return today.year  - self.date_of_birth.year - (( today.month , today.day ) < (self.date_of_birth.month , self.date_of_birth.day))




