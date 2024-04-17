from rest_framework import serializers

from organizations.models import Organization
# from users.serializers import Emplloy


class OrganizationEventSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer(read_only=True, many=True)
    organizations_details = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ('title', 'organizations_details', 'employee')

    def get_organizations_details(self, obj):
        return f'{obj.postcode}, {obj.address}'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'title',
            'description',
            'address',
            'postcode',
        )
