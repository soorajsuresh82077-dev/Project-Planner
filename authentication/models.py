from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    DEVELOPER = 'Developer','Developer'

    ADMIN = 'Admin','Admin'

    PROJECT_COORDINATOR = 'Project Coordinator','Project Coordinator'

class TechChoices(models.TextChoices):

    FRONTEND = 'Frontend Developer','Frontend Developer'

    BACKEND = 'Backend Developer','Backend Developer'

    FULLSTACK = 'Fullstack developer','Fullstack Developer '

    UILX = 'UI/UX Designer','UI/UX Designer'

    TESTER = 'Software Tester','Software Tester'


class Profile(AbstractUser):

    role = models.CharField(max_length=20,choices=RoleChoices.choices)

    tech = models.CharField(max_length=20, choices=TechChoices.choices, blank=True, null=True)

    
    class Meta:

        verbose_name = 'Profiles'

        verbose_name_plural ='Profiles'



    def __str__(self):

        return f'{self.username}--{self.role}--{self.tech}'


   