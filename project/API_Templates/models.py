from django.db import models
from django.contrib.auth import get_user_model


USER = get_user_model()


class ApiTemplate(models.Model):
    body = models.CharField(verbose_name="Template body", max_length=512)
    user = models.ForeignKey(USER, verbose_name="User", on_delete=models.CASCADE)
