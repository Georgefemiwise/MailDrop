from rest_framework import serializers
from .models import Student, Program, Department


class ProgramSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Program
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(required = False)

    class Meta:
        model = Student
        fields = "__all__"
