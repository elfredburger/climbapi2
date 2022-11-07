from django.contrib import admin
from bouldering.models import Boulder,BoulderGrade,BoulderSafety,BoulderLocation,BoulderSector
admin.site.register(Boulder)
admin.site.register(BoulderGrade)
admin.site.register(BoulderSafety)
admin.site.register(BoulderLocation)
admin.site.register(BoulderSector)
# Register your models here.
