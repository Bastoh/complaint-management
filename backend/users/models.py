from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "admin", "Admin"
        HANDLER = "handler", "Handler"
        COMPLAINANT = "complainant", "Complainant"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.COMPLAINANT
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

    def is_admin(self):
        return self.role == self.Roles.ADMIN

    def is_handler(self):
        return self.role == self.Roles.HANDLER

    def is_complainant(self):
        return self.role == self.Roles.COMPLAINANT
