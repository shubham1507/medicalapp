from django.contrib import admin
from .models import *


@admin.register(Company, Medicine, MedicalDetails, Employee, Customer, Bill,
                EmployeeSalary, BillDetails, CustomerRequest, CompanyAccount,
                CompanyBank, EmployeeBank)
class AppAdmin(admin.ModelAdmin):
    pass