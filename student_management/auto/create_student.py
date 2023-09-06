
import time
import json
from student_management.models import Student, Program


from rest_framework.decorators import api_view
from rest_framework.response import Response
# Program = [
#     {
#         "id": 1,
#         "name": "btech",
#         "abbreviation": "bc"
#     },
#     {
#         "id": 2,
#         "name": "diptech",
#         "abbreviation": "pd"
#     },
#     {
#         "id": 3,
#         "name": "hnd",
#         "abbreviation": "07"
#     }
# ]


CURRENT_YEAR = time.strftime('%Y')



@api_view(['GET'])
def test(request):
    print('test')
    return Response({})

@api_view(['GET'])
def create_student(request):
    r"creat student"
    index =20  
    program = 'hnd'
    course = 'ict'
    
    # generate_email = createEmailAddress(index, CURRENT_YEAR[2:], program)
    
    # program_abbreviation = ''
    
    # newIndex = get_index(program, index)

    # graduation = calculateGraduationDate(program)
    
    # academic_year = CURRENT_YEAR
    
    
    # if not Student.objects.filter(email=generatedEmail).exists():
    #     program = get_object_or_404(Program, abbreviation__iexact=program_name)
        
        
        
        # newStudent = Student(
		# 	index = newIndex,
		# 	program = 'program',
		# 	email = generate_email,
		# 	level = 11,
		# 	year_enrolled = CURRENT_YEAR,
		# )
        # newStudent.save()
        # print("done")
    return Response({})
        





# def createEmailAddress(index: any, year: any, program: str):
#     r"""Create a new email address"""

#     programAbbrv = 'bc'
    
#     course  = "ict" if program != 'hnd' else '000'
    
#     if program == 'hnd':
#         address = f"{programAbbrv}{CURRENT_YEAR[2:]}{course}{index:03}@ttu.edu.gh"
#         return address
#     else:
#         address = f"{programAbbrv}{course}{year}{index:03}@ttu.edu.gh" 
#         return address


# def get_index( program:str, index:int ): 
#     r"micro function for getting the right formated index number"
    
#     programAbbrv = 'hnd' #[program]
#     department  = "ict" if program != 'hnd' else '000'
    
#     if program != 'hnd':
#         address = f"{programAbbrv}/{department}/{CURRENT_YEAR[2:]}/{index:03}" 
#         return address
    
#     else:
#         address = f"{programAbbrv}{CURRENT_YEAR[2:]}{index:06}"
#         return address
        
        
# def calculateGraduationDate( program:str ):
    
#     thisYear = int(CURRENT_YEAR)
#     if program ==  'diptech':
#         return str(2 + thisYear) 
#     elif program == 'hnd':
#         return str(3 + thisYear)
#     else:
#         return str(4 + thisYear)
    
    
    





