#a script that produces a more structured patient 'freetext' - necessary information for patient letters from consultants and GP's etc. 



Patient_Full_Name = input("What is the patient's full name? ")
date1 = input("What was the date of the appointment? ")
medication1 = input("What is the name of the first medication? ") 
medication2 = input("What is the name of the second medication? ") 
medication3 = input("What is the name of the third medication? ") 
medication4 = input("What is the name of the fourth medication? ") 
medication5 = input("What is the name of the fifth medication? ") 
medication6 = input("What is the name of the sixth medication? ") 
medication7 = input("What is the name of the seventh medication? ") 
date2 = input("What is the date of the next appointment? ")

patient_text = f"{Patient_Full_Name} attended their appointment on {date1}. They are currently taking {medication1}, {medication2}, {medication3},
{medication4}, {medication5}, {medication6}, {medication7}. Their next appointment will be on {date2}.

print(patient_text)
