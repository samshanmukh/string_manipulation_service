from django.urls import path, re_path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'strings', views.StringsViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.api_root),
    path("list/",views.ListStringsAPIView.as_view(),name="strings_list"),
    path("create/", views.CreateStringsAPIView.as_view(),name="strings_create"),
    path("get/<int:id>/",views.GetStringsAPIView.as_view(),name="get_strings"),
    path("update/<int:pk>/",views.UpdateStringsAPIView.as_view(),name="update_strings"),
    path("delete/<int:pk>/",views.DeleteStringsAPIView.as_view(),name="delete_strings"),
    path('string_operations/<int:id>/', views.StringOperationsAPIView.as_view(), name='string_operations'),
]
