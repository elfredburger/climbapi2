from django.db import models
from bouldering.models import Boulder

class AppUser(models.Model):
    username=models.CharField(verbose_name='username',max_length=30,unique=True)
    user_first_name=models.CharField(verbose_name='first name',max_length=30)
    user_second_name=models.CharField(verbose_name='second name',max_length=30)
    user_email=models.EmailField(verbose_name='email',max_length=30)
    user_password=models.CharField(verbose_name='user password',max_length=30)
    user_complete_boulders=models.ManyToManyField(Boulder,verbose_name='complete boulders',related_name='completed_boulders')
    user_fa_boulders=models.ManyToManyField(Boulder,verbose_name='FA boulders',related_name='fa_boulders')
    user_found_boulders=models.ManyToManyField(Boulder,verbose_name='boulders found',related_name='found_boulders')
    user_favorite_boulders=models.ManyToManyField(Boulder,verbose_name='favorite boulders',related_name='favorite_boulders')
    user_about=models.CharField(max_length=500,verbose_name='about me')
    user_profile_pic=models.ImageField(upload_to='static/users/images/', null=True, blank=True,verbose_name='profile picture')
    def __str__(self):
        return self.username
