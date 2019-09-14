from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Coupon(models.Model):

    code = models.TextField()
    already_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    used_by_seller = models.ForeignKey(User, unique=False, on_delete=models.CASCADE, blank=True, null=True)

