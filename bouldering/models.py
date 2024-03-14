from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class BoulderLocation(models.Model):
    location_name=models.CharField(max_length=50,default=1,verbose_name='location name',blank=False,unique=True)
    location_info=models.CharField(max_length=400,default='everything is obvious',verbose_name='additional information about boulder',blank=False)

    def __str__(self):
        return self.location_name
    class Meta:
        verbose_name='Location'
        verbose_name_plural='Locations'


class BoulderGrade(models.Model):
    boulder_grade=models.CharField(max_length=10,blank=False,unique=True)

    def __str__(self):
        return self.boulder_grade
    class Meta:
        verbose_name='Boulder grade'
        verbose_name_plural='Boulder grades'


class BoulderSafety(models.Model):
    safety_grade=models.IntegerField(choices=[(i,i) for i in range(11)],unique=True)

    def __str__(self):
        return str(self.safety_grade)

    class Meta:
        verbose_name='Safety grade'
        verbose_name_plural='Safety grades'

class BoulderSector(models.Model):
    sector_name=models.CharField(max_length=50,default=1,verbose_name='sector name',blank=False)
    sector_location=models.ForeignKey(BoulderLocation, verbose_name='sector location',on_delete=models.SET_DEFAULT,default=1,blank=True,null=True)
    sector_coords=models.CharField(max_length=200,verbose_name='sector coordinates from google maps', default=1,blank=True,null=True )

    def __str__(self):
        return self.sector_name
    class Meta:
        verbose_name='Sector'
        verbose_name_plural='Sectors'
        
class BoulderPhoto(models.Model):
    class Meta:
        verbose_name='Boulder Photo'
        verbose_name_plural='Boulder Photos'
    photo =  models.ImageField(upload_to='static/boulders/images/', null=True, blank=True,verbose_name="Фото")


class Boulder(models.Model):
    def __str__(self):
        return self.boulder_name
    def get_boulder_name(self):
        return str(self.boulder_name)
    class Meta:
        verbose_name='Boulder'
        verbose_name_plural='Boulders'



    boulder_name=models.CharField(max_length=50,verbose_name='boulder name',blank=False)
    boulder_finder=models.ForeignKey(User,blank=True,null=True,verbose_name='boulder finder',on_delete=models.SET_DEFAULT,default=1)
    boulder_grade=models.ForeignKey(BoulderGrade,blank=False,verbose_name='boulder grade',on_delete=models.SET_DEFAULT,default=1)
    boulder_safety=models.ForeignKey(BoulderSafety,blank=False,verbose_name='boulder safety level', on_delete=models.SET_DEFAULT,default=1)
    boulder_sector=models.ForeignKey(BoulderSector,null=True,blank=True,verbose_name='sector where boulder is located',on_delete=models.SET_DEFAULT,default=1)
    boulder_coords = models.URLField(max_length=1000, blank=True, verbose_name='Ссылка на локацию трассы', help_text='Принимаются метки с гугл карт', null=True)
    boulder_photos=models.ManyToManyField(BoulderPhoto)
    boulder_info=models.CharField(max_length=300,blank=True,null=True,verbose_name='information about a boulder',default='no information')
    boulder_location=models.ForeignKey(BoulderLocation,blank=False,verbose_name='boulder location',on_delete=models.SET_DEFAULT,default=1)

