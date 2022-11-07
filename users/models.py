from django.db import models
from bouldering.models import Boulder
from django.contrib.auth.models import User, AbstractUser
from django import forms
from datetime import date


        #THIS CUSTOM USER MODEL TO BE IMPLEMENTED

class AppUser(models.Model):
    ROLES=()
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    user_complete_boulders=models.ManyToManyField(Boulder,verbose_name='complete boulders',related_name='completed_boulders',blank=True)
    user_fa_boulders=models.ManyToManyField(Boulder,verbose_name='FA boulders',related_name='fa_boulders',blank=True)
    user_found_boulders=models.ManyToManyField(Boulder,verbose_name='boulders found',related_name='found_boulders',blank=True)
    user_favorite_boulders=models.ManyToManyField(Boulder,verbose_name='favorite boulders',related_name='favorite_boulders',blank=True)
    user_about=models.CharField(max_length=500,verbose_name='about me',blank=True)
    user_profile_pic=models.ImageField(upload_to='static/users/images/', null=True, blank=True,verbose_name='profile picture')
    user_poster=models.BooleanField(default=False,blank=True)
    def __str__(self):
        return str(self.user.username)
