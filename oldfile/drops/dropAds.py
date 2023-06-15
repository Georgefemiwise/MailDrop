# from schoolMailGenerator.AddressBoiler import EmailAdsBoiler
# from .models import BachelorsDegreeAddresses as BDA



# class DropAddress(EmailAdsBoiler): 
#      #inherites from Generate email.
#      # not a view class
#      def __init__(self, program:str, year:int, numInClass:int):
#           super().__init__(program, year)
#           self.numInClass = numInClass


#      def genAddress(self):
#           # key email generator
#           # it generate Bachelors degree student email only
#           for num in range(1,int(self.numInClass)+1):
#                generating = f"{self.program}{str(self.year)}{num:03}@ttu.edu.gh"
               
#                if BDA.objects.filter(Address=generating).exists(): 
#                     #checking if the email exists in the database
#                     #if it dose it updates it this way there wont be dupplicates in the database
#                     address = BDA.objects.create(Address=generating)
#                     address.save(force_update=True)
          
#                else:
#                     address = BDA.objects.create(Address=generating)
#                     address.save
man = 'True'

if  'True' not in man:
     print('True')
else: 
     print('woman')
