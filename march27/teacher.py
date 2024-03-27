class Teacher:
    teacherList = []

    def __init__(self,name,surname,field) -> None:
        self.name = name
        self.surname = surname
        self.field = field
        print("Öğretmen başlangıç çalıştı")
        
    def teacherInfo(self):
      person= (self.name+" "+ self.surname+" "+ self.field)
      Teacher.teacherList.append(person)
      for info in Teacher.teacherList:
        print(info) 