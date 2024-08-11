from django.urls import path,include
from . import views
from .views import studentviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r"student",studentviewset)
urlpatterns = [

    path("",views.welcome,name="خوش آمدگویی"),
    path('',include(router.urls)),

]

