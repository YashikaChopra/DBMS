from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views
from .views import AttendanceViewSet
from .views import CreateUserViewSet 
from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'register',views.CreateUserViewSet,basename='s')
router.register(r'profile',views.UserProfileViewSet)
router.register(r'pro2', ProfileViewSet, basename='profile_api')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    

] 