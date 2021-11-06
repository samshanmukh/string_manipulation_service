from django.urls import path, re_path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'strings', views.StringsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.home, name='blog-home'),
    # path('about/', views.about, name='blog-about'),
]
