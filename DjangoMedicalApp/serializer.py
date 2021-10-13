
from rest_framework import serializers

from DjangoMedicalApp.models import Company, CompanyBank


class CompanySerializer( serializers.ModelSerializer ):
    class Meta:
        model = Company
        fields = ["name","license_no","address","contact_no","email","description"]

class CompanyBankSerializer( serializers.ModelSerializer ):
    class Meta:
        model = CompanyBank
        fields = ["bank_account_no","ifsc_no","company_id"]

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['Company']=CompanySerializer(instance.company_id).data
        return response

