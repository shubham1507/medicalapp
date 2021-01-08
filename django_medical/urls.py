from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from DjangoMedicalApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from DjangoMedicalApp.views import CompanyViewSet, CompanyBankViewSet, CompanyNameViewSet, MedicineViewSet
router = routers.DefaultRouter()

router.register("company", views.CompanyViewSet, basename="company")
router.register("companybank",
                views.CompanyBankViewSet,
                basename="companybank")

router.register("medicine", views.MedicineViewSet, basename="medicine")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/resfresh_token/',
         TokenRefreshView.as_view(),
         name="refresh_token"),
    path('api/companybyname/<str:name>',
         CompanyNameViewSet.as_view(),
         name="companybyname"),
]
