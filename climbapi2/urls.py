"""climbapi2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bouldering import views
from users import views as views2

urlpatterns = [
    path('admin/', admin.site.urls), #Admin endpoint

    path('api/v1/boulders/', views.AllBoulders.as_view()),#List of all boulders ListCreate
    path('api/v1/boulders_user/',views.BouldersByUser.as_view()),#Boulders found by logged in user List
    path('api/v1/boulder/id=<int:id>', views.BoulderByIdUser.as_view()),#Boulder by id for user List
    path('api/v1/admin/boulder/id=<int:id>', views.BoulderByIdAdmin.as_view()),#Boulder by id by any user(admin only) RetriveUpdateDestroy
    path('api/v1/boulders/grade=<str:boulder_grade>', views.BouldersByGrade.as_view()),# List of boulders by grade List
    path('api/v1/boulders/grade=<str:boulder_grade>/location=<str:boulder_location>',
         views.BouldersByGradeLocation.as_view()),# List of boulders by grade and location List
    path('api/v1/boulders/grade=<str:boulder_grade>/sector=<str:boulder_sector>/location=<str:boulder_location>',
         views.BouldersByGradeSectorLocation.as_view()),# list of  boulders by grade, sector, location List
    path('api/v1/boulders/safety=<str:boulder_safety>/sector=<str:boulder_sector>',
         views.BouldersBySafetySector.as_view()), # list of boulders by safety and sector List
    path('api/v1/boulders/location=<str:boulder_location>', views.BouldersByLocation.as_view()), # List of boulders by location List
    path('api/v1/boulders/location=<str:boulder_location>/sector=<str:boulder_sector>',
         views.BouldersByLocationSector.as_view()), # list of boulders  by location and sector List
    path('api/v1/boulders/finder=<str:boulder_finder>', views.BouldersByFinder.as_view()),# List of boulders by specific finder List
    path('api/v1/boulders/name=<str:boulder_name>', views.BouldersByName.as_view()), # list of boulders  with specific name List
    path('api/v1/boulders/safety=<str:boulder_safety>/location=<str:boulder_location>/sector=<str:boulder_sector>',
         views.BouldersBySafetyLocationSector.as_view()),# list of boulders by safety, location, sector List
    path('api/v1/boulders/safety=<str:safety_grade>/location=<str:location_name>',
         views.BouldersBySafetyLocation.as_view()),# list of boulders by safety and location List
    path('api/v1/boulders/safety=<str:safety_grade>', views.BouldersBySafety.as_view()),# list of boulders by safety List
    path('api/v1/boulders/safety=<str:safety_grade>/grade=<str:boulder_grade>', views.BouldersBySaftetyGrade.as_view()),# list of boulers by safety and grade List
    path('api/v1/boulders/safety=<str:safety_grade>/grade=<str:boulder_grade>/location=<str:location_name>',
         views.BouldersBySafetyGradeLocation.as_view()),# list of boulders by safety, grade, location List
    path('api/v1/boulders/safety=<str:safety_grade>/grade=<str:boulder_grade>/location=<str:location_name>/sector=<str:boulder_sector>',
         views.BouldersBySafetyGradeLocationSector.as_view()), # list of boulders by safety, grade, location, sector List

    path('api/v1/sectors', views.BoulderSectorAll.as_view()),# list of all sectors ListCreate
    path('api/v1/admin/sector_create',views.BoulderSectorCreate.as_view()),#Create bouldering sector Create
    path('api/v1/sectors/location=<str:location_name>', views.BoulderSectorByLocation.as_view()), # list of sectors in a location List
    path('api/v1/sectors/sector=<str:sector_name>', views.BoulderSectorByName.as_view()), # list of sectors by name List
    path('api/v1/sector/id=<int:id>', views.BoulderSectorById.as_view()), # boulder sector by id for user List
    path('api/v1/admin/sector/id=<int:id>', views.BoulderSectorByIdAdmin.as_view()), # boulder sector by id for admin RetriveUpdateDestroy

    path('api/v1/locations', views.BoulderLocationAll.as_view()), # list of all locations ListCreate
    path('api/v1/locations/name=<str:location_name>', views.BoulderLocationByName.as_view()),# list of locations by name List
    path('api/v1/location/id=<str:id>',views.BoulderLocationByIdUser.as_view()),
    path('api/v1/admin/location/id=<str:id>',views.BoulderLocationByIDAdmin.as_view()), # editing location for admin RetriveUpdateDestroy

    path('api/v1/safetygrades', views.BoulderSafetyAll.as_view()), # list of all safety grades List
    path('api/v1/admin/safetygrade/id=<int:id>',views.BoulderSafetyByIdAdmin.as_view()),


    path('api/v1/grades', views.BoulderGradeAll.as_view()), # list of all safety grades List
    path('api/v1/grade/id=<int:id>', views.BoulderGradeById.as_view()), # boulder grade by id List
    path('api/v1/admin/grade/id=<int:id>', views.BoulderGradeByIdAdmin.as_view()), # boulder grade by id for admin RetriveUpdateDestroy

    path('api/v1/users', views2.UserAll.as_view()),#List of all users ListCreate
    path('api/vq/users/username=<str:username>', views2.UserByUsername.as_view()),# User by username List
    path('api/v1/user/email=<str:email>', views2.UserByEmail.as_view()),#User by email List
    path('api/v1/user/id=<int:id>', views2.UserById.as_view()), # User by Id Retriveupdatedestroy Listcreate
    path('api/v1/users/first_name=<str:first_name>', views2.UsersByFirstName.as_view()),
    path('api/v1/users/last_name=<str:last_name>', views2.UsersByLastName.as_view()),
    path('api/v1/users/first_name=<str:first_name>&last_name=<str:last_name>', views2.UsersByFullName.as_view()),

    path('api/v1/users_info', views2.AppUsers.as_view()),
    path('api/v1/user_climbed/id=<int:user_id>', views2.UsersClimedBoulder.as_view()),
    path('api/v1/user_fa/id=<int:user_id>', views2.UserFaBoulders.as_view()),
    path('api/v1/user_fav/id=<int:user_id>', views2.UserFavoriteBoulders.as_view()),
    path('api/v1/user_found/id=<int:user_id>', views2.UserFoundBoulders.as_view()),

]
