from django.contrib import admin
from bouldering.models import Boulder,BoulderGrade,BoulderFinder,BoulderSafety,BoulderLocation,BoulderSector
from users.models import AppUser
admin.site.register(Boulder)
admin.site.register(BoulderGrade)
admin.site.register(BoulderFinder)
admin.site.register(BoulderSafety)
admin.site.register(BoulderLocation)
admin.site.register(BoulderSector)
admin.site.register(AppUser)
# Register your models here.
