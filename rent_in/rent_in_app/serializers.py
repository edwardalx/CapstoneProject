from rest_framework import serializers
from .models import Tenant, Property, Tenancy_Agreement

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        feilds = '__all__'
    def get_full_name(self, obj):
        return obj.first_name + " "+ obj.last_name

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        feilds = '__all__'

class TenancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Tenancy_Agreement
        feilds = '__all__'
    
    def create(self, validated_data):
        phone_no_data = validated_data.pop('phone_no')
        property_data = validated_data.pop('property_name')

        # Get or create the property instance
        property_instance, _ = Property.objects.get_or_create(**property_data)

        # Create the tenancy agreement
        tenancy_agreement = Tenancy_Agreement.objects.create(property_name=property_instance, **validated_data)

        # Add tenants to ManyToMany field
        for tenant_data in phone_no_data:
            tenant, _ = Tenant.objects.get_or_create(**tenant_data)
            tenancy_agreement.phone_no.add(tenant)

        return tenancy_agreement

    def update(self, instance, validated_data):
        phone_no_data = validated_data.pop('phone_no', None)
        property_data = validated_data.pop('property_name', None)

        # Update property if provided
        if property_data:
            property_instance, _ = Property.objects.get_or_create(**property_data)
            instance.property_name = property_instance

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        # Update ManyToMany phone_no field
        if phone_no_data is not None:
            instance.phone_no.clear()  # Remove existing tenants
            for tenant_data in phone_no_data:
                tenant, _ = Tenant.objects.get_or_create(**tenant_data)
                instance.phone_no.add(tenant)

        return instance