from rest_framework import serializers
from .models import JoinMT, Contact

class JoinMTSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinMT
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
