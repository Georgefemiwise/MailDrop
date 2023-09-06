
import time

from student_management.models import Student, Program


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer


CURRENT_YEAR = time.strftime('%Y')




@api_view(['POST'])
def create_student(request):
    
    amount = 10
    program = 'btech'
    
    
    def genEmail(index):
        index.replace('/', '')
        address = f"{index}@ttu.edu.gh"
        return address
        
       
    
    def genIndex( program:str, index:int ):
        
        if program == 'hnd':
            abviation = '07'
            
        elif program == 'diptech':
            abviation = 'pd'
            
        else:
            abviation = 'bc'
        
        
        course = 'ict' if program != 'hnd' else ''
        
        if program != 'hnd':
            address = f"{abviation}{course}{CURRENT_YEAR[2:]}{index:03}"
            return address
        
        else:
        	address = f"{abviation}{CURRENT_YEAR[2:]}{index:06}"
        return address
    
    
    def calGraduation(program):
        thisYear = int(CURRENT_YEAR)
        if program ==  'diptech':
            return str(2 + thisYear)
        
        elif program == 'hnd':
            return str(3 + thisYear)
        
        else:
            return str(4 + thisYear)
       
    students_data = []
    # serializer = StudentSerializer
    for index in range(1, amount + 1):
        newindex = genIndex(program=program, index=index)
        email = genEmail(index = newindex )
        grads = calGraduation(program)
        newProgram = Program.objects.get(program_name=program)
        newStudent= Student(
			index=newindex,
			email= email,
			program=newProgram,
			
			)
        newStudent.save()
    
    student_serializer = StudentSerializer(newStudent)
    students_data.append(student_serializer.data)
    
    return Response({'students': students_data})




@api_view(['GET'])
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        # Retrieve the serialized data
        serialized_students = serializer.data
 
        # Add email and index fields to each student
        for student_data in serialized_students:
            student = Student.objects.get(id=student_data['id'])
            program = student.program
            program_data = {
                
                'abbreviation' : program.program_abbreviation,
                'program_name' : program.program_name,
                'department' : program.department.department_name,
                'faculty' : program.department.faculty.faculty_name,
                'department' : program.department.department_name,
            }
            student_data['program'] = program_data
            student_data['email'] = student.email
            student_data['index'] = student.index

        # Return the updated serialized students as a response
        return Response(serialized_students)

      

