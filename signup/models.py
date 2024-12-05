from django.core.exceptions import ValidationError
from django.db import models


def validate_only_strings(value):
    if not value.isalpha():
        raise ValidationError('User name must contain only letters.')
    

class User(models.Model):
    user_name = models.CharField(max_length=50, validators=[validate_only_strings])

    def __str__(self):
        return self.user_name