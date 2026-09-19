from pydantic import BaseModel
from typing import Optionai

class Student(BaseModel):
    name:str="Default Name"
    age:Optionai[int]=None
    email:Emailstr
    cgpa:float= Field(gt=0,lt=10,description='adhhj')#constraints&deafult values also
    

new_student={'name':'Ruchika','email':'ruchika@example.com','cgpa':8.5} 

student=Student(**new_student)
print(student.name)
student_dict=dict(student)
print(student_dict['age'])

#also in json
student_json=student.model_dump_json()
