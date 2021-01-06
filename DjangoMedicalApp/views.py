from rest_framework import viewsets, generics
from .models import Company
from .serilaizers import CompanySerliazer


class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerliazer
