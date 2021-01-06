from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from DjangoMedicalApp import views

from DjangoMedicalApp.views import CompanyViewSet
router = routers.DefaultRouter()

router.register("company", views.CompanyViewSet, basename="company")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
