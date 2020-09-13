

from rest_framework import serializers


from .models import UserManagement

class AddRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserManagement
        fields = ("name",'mobile','email','gender')

        