from django.db import models
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


def get_or_create_profile(user):
    try:
        profile, created = UserProfile.objects.get_or_create(user=user)
        return profile
    except IntegrityError:
        
        return UserProfile.objects.filter(user=user).first()

User.add_to_class("get_or_create_profile", get_or_create_profile)