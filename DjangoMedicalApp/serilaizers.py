from rest_framework import serializers
from DjangoMedicalApp.models import Company, CompanyBank, Medicine, MedicalDetails, Employee, Customer, Bill, \
    CustomerRequest, CompanyAccount, EmployeeBank, EmployeeSalary, BillDetails


class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
