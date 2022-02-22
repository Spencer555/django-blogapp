from pickletools import optimize
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage
from django.dispatch import receiver
from django.db.models.signals import post_save
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'    
    

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     image = Image.open(self.image.path)
    #     image.save(self.image.path, quality=10, optimize=True)
    #     return self


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
