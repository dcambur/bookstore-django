from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    TITLE_MAX_LENGTH = 64
    NAME_MAX_LENGTH = 32
    DESCRIPTION_MAX_LENGTH = 1024

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH)
    author = models.CharField(max_length=NAME_MAX_LENGTH)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} --- published by: {self.published_by}"