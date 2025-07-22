from rest_framework import serializers
from api.models import Student
from rest_framework.validators import ValidationError
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id' , 'name' , 'roll' , 'city']
    
    def validate_name(self , value):
        if len(value) > 3:
            raise ValidationError('Enter small name')
        return value