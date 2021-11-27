from django.db import models
from django.core.validators import(
    EmailValidator,validate_email
)

class Contact(models.Model):
    email = models.CharField(max_length=200, default="test@test.ru",validators=[
        EmailValidator(
            message="Введите корректный email"
        )
    ])
    message = models.CharField(max_length=200, default="some_message") 


def __str__(self):
    return self.email