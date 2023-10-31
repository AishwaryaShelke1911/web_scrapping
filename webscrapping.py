# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 23:17:43 2023

@author: Aishwarya
"""

class student:
    def__init__(self,student_id,name,age,grade):
        self,student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        
class school:
   def _ _init_ _(self,name):
       self.name = name
       self.students = []
       
   def add_student(self,student):
       self.students.append(student)
       
   def remove_student(self, student_id):
       for student in self.students:
           if student.student_id == student_id:
               self.students.remove(student)
               print(f"students in {student_id} removed")
               return
       print(f"student with ID {student_id} not found.")
       
   def list_students(self):
       print(f"students in {self.name} school:")
       for student in self.students:
           print(f"ID: {student.student_id}, name: {student.name}, age: {student.age}, grade: {student.grade}")
           
# sample usage
if _ _name_ _== "_ _main_ _":
     school = school("example school")

student1 = student(1, "Alice", 16, "A")
student2 = student(2, "Bob", 15, "B")
student3 = student(3, "Charlie", 17, "A")

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

school.list_students()

school.remove_student(2)

school.list_students()       