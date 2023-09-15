from rest_framework import serializers
from .models import Student, Program, Department


class ProgramSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Program
        fields = ["program_name", "program_abbreviation", "department", ]


class StudentSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(required = False)

    class Meta:
        model = Student
        fields = ["id", "index", "email", "isInSchool", "year_enrolled", "graduation_date", "level", "program",]
    
