from rest_framework import serializers
from .models import Student, Program, Department

class ProgramSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Program
        fields = ['name', 'department']


class StudentSerializer(serializers.ModelSerializer):
    program = ProgramSerializer()  # Include ProgramSerializer as a nested serializer

    class Meta:
        model = Student
        fields = ['id', 'program', 'level', 'year_enrolled', 'name', ]

