class Student:
     midtermNote = 0
     finalNote = 0
     studentList = []

     def __init__(self,name,surname,studentNo) -> None:
          self.name = name
          self.surname = surname
          self.studentNo = studentNo
          print(f"Hoşgeldin {self.name} {self.surname}")
          
     def gradeCalculation(self,midtermNote,finalNote):
          self.midtermNote = midtermNote
          self.finalNote = finalNote
          total = (self.midtermNote * 0.4) + (self.finalNote * 0.6)
          print(f"Ortalamanız : {total}")
          
     def studentInfo(self):
          person = (self.name+" "+ self.surname+" "+ self.studentNo)
          Student.studentList.append(person)
          for info in Student.studentList:
               print(info) 
        