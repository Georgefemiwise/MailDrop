# Import necessary modules and classes
from schoolMailGenerator.AddressBoiler import EmailAdsBoiler
from .models import BachelorsDegreeAddresses as BDA

# Define a class to generate and save email addresses
class DropAddress(EmailAdsBoiler):
     def __init__(self, program:str, year:int, numInClass:int):
          super().__init__(program, year)
          self.numInClass = numInClass

     def genAddress(self):
          # Generate and save email addresses for Bachelors degree students
          for num in range(1,int(self.numInClass)+1):
               generating = f"{self.program}{str(self.year)}{num:03}@ttu.edu.gh"
               
               if BDA.objects.filter(Address=generating).exists(): 
                    # If the email address already exists, update the existing record
                    address = BDA.objects.get(Address=generating)
                    address.save(force_update=True)
               else:
                    # Otherwise, create a new record
                    address = BDA.objects.create(Address=generating)
                    address.save() # Add parentheses to save the new record to the database
          

# ============================================================================================================

# Import necessary modules and classes
from schoolMailGenerator.AddressBoiler import EmailAdsBoiler
from .models import BachelorsDegreeAddresses as BDA

# Define a class to generate and save email addresses
class DropAddress(EmailAdsBoiler):
     def __init__(self, program:str, year:int, numInClass:int):
          super().__init__(program, year)
          self.numInClass = numInClass

     def genAddress(self):
          # Generate and save email addresses for Bachelors degree students
          for num in range(1,int(self.numInClass)+1):
               generating = f"{self.program}{str(self.year)}{num:03}@ttu.edu.gh"
               
               if not BDA.objects.filter(Address=generating).exists(): 
                    # If the email address does not already exist, create a new record
                    address = BDA.objects.create(Address=generating)
                    address.save() # Add parentheses to save the new record to the database
