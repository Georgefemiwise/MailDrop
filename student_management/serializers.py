from rest_framework import serializers
from .models import Student, Program, Department



class ProgramSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Program
        fields = ['name', 'department', 'abbreviation']


class StudentSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(required=False)

    class Meta:
        model = Student
        fields = ['id', 'program', 'level', 'year_enrolled', 'name']
        extra_kwargs = {
            'program': {'required': False},
        }
