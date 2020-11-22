from rest_framework import routers
from .views import UserViewSet
from . import views
from django.urls import path,include

router=routers.DefaultRouter()
router.register('', views.UserViewSet)
urlpatterns=[
    path('login/', views.signin, name="sign_in"),
    path('logout/<int:id>/',views.signout, name="sign_out"),
    path('', include(router.urls))
]