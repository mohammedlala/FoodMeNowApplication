from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    mobile = models.BigIntegerField(null=False)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()

class Requirement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    times = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    food = models.CharField(max_length=10)
    food_category = models.TextField()
