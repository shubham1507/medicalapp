from rest_framework import serializers
from DjangoMedicalApp.models import Company, CompanyBank, Medicine, MedicalDetails, Employee, Customer, Bill, \
    CustomerRequest, CompanyAccount, EmployeeBank, EmployeeSalary, BillDetails


class CompanySerlizer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanyBankSerlizer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerlizer(instance.company_id).data
        return response


class MedicineSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"

    def to_representation(self, instance):
        print("to_representation has been called")
        response = super().to_representation(instance)
        response['company'] = CompanySerlizer(instance.company_id).data
        return response


class MedicalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = "__all__"

    def to_representation(self, instance):
        print("to_representation has been called")
        response = super().to_representation(instance)
        response['medicine'] = MedicineSerliazer(instance.medicine_id).data
        return response


class EmployeeSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CustomerSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def to_representation(self, instance):
        print("to_representation has been called")
        response = super().to_representation(instance)
        response['customer'] = CustomerSerlizer(instance.customer_id).data
        return response


class CustomerRequestSerlizer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = "__all__"


class CompanyAccountSerlizer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = "__all__"

    def to_representation(self, instance):
        print("to_representation has been called")
        response = super().to_representation(instance)
        response['customer'] = CompanySerlizer(instance.customer_id).data
        return response


class EmployeeBankSerlizer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        fields = "__all__"

    def to_representation(self, instance):
        print("to_representation has been called")
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerlizer(instance.employee_id).data
        return response