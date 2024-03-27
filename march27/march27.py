from student import Student 
from teacher import Teacher # teacher dosyasından Teacher class'ının içindekileri burada kullanalım

isStudent = False

while True :
    try :    
        who = int(input("Öğrenci iseniz 1'e Öğretmenseniz 2'ye basınız ! "))
        if who == -1:
            break

        name = input("Adınızı Girin: ")
        surname = input ("Soyadınızı Girin: ")

        if who == 1 :
            studentNo = input("Öğrenci Numaranızı Girin: ")
            student = Student(name,surname,studentNo)
            isStudent = True
            if isStudent:
                midtermNote = float(input("Vize Notunu Girin: "))
                finalNote = float(input("Final Notunu Girin: "))
                student.gradeCalculation(midtermNote,finalNote)    
            student.studentInfo()    
        else:
            field = input("Alanınızı Girin: ")
            teacher = Teacher(name,surname,field)
            teacher.teacherInfo()

    except  KeyboardInterrupt: # Kod çalışırken 'ctrl + c' ile durdurmak için 
        break   
    except Exception as e:     # Hata aldığımızda hatayı ekrana basmak için
        print(f"Error : {e}")