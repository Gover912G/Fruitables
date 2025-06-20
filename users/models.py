from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField()
    image = models.ImageField(default = 'default.png', upload_to='Profile_pic')


    def __str__(self):
        return f'{self.user.username} profile'
    