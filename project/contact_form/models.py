from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=200, default="test@test.ru")
    message = models.CharField(max_length=200, default="some_message") 


def __str__(self):
    return self.email