from rest_framework import serializers
from .models import Tenant, Property


class TenantSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Tenant
        fields = '__all__'+ ('full_name',)
    
    def get_full_name(self, obj):
        return obj.first_name + " "+ obj.last_name
    

    
