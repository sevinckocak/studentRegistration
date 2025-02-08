print("""************************************
PLEASE SELECT THE TRANSACTİON:
1. List all the courses
2. Courses with students in them
3. Add a new course
4. Search a course by course code
5. Search a course by course name
6. Register a student to a course
7. 3 Most crowded course
8. To exit the transaction
**********************************""")
def all_courses():
    with open("course.txt","r",encoding="utf-8") as file:
        datas = file.readlines()
        for atlama in datas:
            atlama=atlama.replace("\n","")
            atlama=atlama.split(";")
            print(atlama[1])
def course_with_student():
    course_with_student=list()
    with open("course.txt",encoding="utf-8") as least:
        i=least.readlines()
        for atlama1 in i:
            atlama1=atlama1.replace("\n","")
            atlama1=atlama1.split(";")
            if int(atlama1[3])>0 :
                course_with_student.append(atlama1[1])
    print(course_with_student)
def add_new_course():
    with open("course.txt", "a", encoding="utf-8") as ekleme:
        a = input("Write the course code:")
        b = input("Write the lesson name:")
        c = input("Write the teachers's name:")
        bilgiler = [a, b, c]
        birleştirme = ("{} ; {} ; {} ;0\n".format(bilgiler[0], bilgiler[1], bilgiler[2]))
        ekleme.write(birleştirme)
def course_code_search():
    word = input("Please enter the code of the lesson:")
    with open("course.txt", encoding="utf-8") as arama:
        kelime = arama.read()
        if word in kelime:
            print("Lesson Code is Found:", word)
        else:
            print("Lesson Code is Not Found")
def course_name_search():
    word2 = input("Please enter name of the lesson:")
    with open("course.txt","r", encoding="utf-8") as arama2:
        gezinsin = arama2.readlines()
        for atlama2 in gezinsin:
            atlama2 = atlama2.replace("\n", "")
            atlama2 = atlama2.split(";")
            if word2 in atlama2[1]:
                print("Lesson name:",atlama2[1])
def student_register():
    studentname = input("Please write student name:")
    studentsurname = input("Please write student surname:")
    studentıd = input("Please write student ID:")
    studentcourse = input("Please write course:")
    bilgiler2 = [studentıd, studentname, studentsurname, studentcourse]
    birleştirme2 = ("{};{} {};{}\n".format(bilgiler2[0], bilgiler2[1], bilgiler2[2], bilgiler2[3]))
    with open("student.txt", "a", encoding="utf-8") as ekleme:
        ekleme.write(birleştirme2)
    bosliste = list()
    with open("course.txt", "r", encoding="utf-8") as sayıdeğiştirme:
        işlemöncesi = sayıdeğiştirme.readlines()
        for atlama3 in işlemöncesi:
            atlama3 = atlama3.replace("\n", "")
            atlama3 = atlama3.split(";")
            if studentcourse in atlama3[0]:
                eskimevcut = int(atlama3[3])
                yenimevcut = eskimevcut + 1
                print("Changed old class size from", eskimevcut, "to", yenimevcut)
def crowded_class():
    with open("course.txt","r", encoding="utf8") as dosyaacımı:
        okusun=dosyaacımı.readlines()
        listeleyelim=[]
        for dolassın in okusun:
            dolassın=dolassın.strip()
            sınıfbilgisi=dolassın.split(";")
            listeleyelim.append(int(sınıfbilgisi[3]))
        listeleyelim.sort(reverse=True)
        listeleyelim=listeleyelim[:3]
        for dolassın in okusun:
            dolassın=dolassın.strip()
            sınıfbilgisi=dolassın.split(";")
            if int(sınıfbilgisi[3]) in listeleyelim:
                print(sınıfbilgisi[0],sınıfbilgisi[1],sınıfbilgisi[2])

import time
while True:
    islem_secimi=int(input("Please enter your transaction:"))
    if islem_secimi==1:
        print("The transaction is being performed...")
        time.sleep(1)
        print("All Courses:")
        print(all_courses())
    elif islem_secimi==2:
        print("The transaction is being performed...")
        time.sleep(1)
        print("Courses with students in them:")
        print(course_with_student())
    elif islem_secimi==3:
        print("The transaction is being performed...")
        time.sleep(1)
        print("Add a new course:")
        print(add_new_course())
    elif islem_secimi==4:
        print("The transaction is being performed...")
        time.sleep(1)
        print(course_code_search())
    elif islem_secimi==5:
        print("The transaction is being performed...")
        time.sleep(1)
        print("Which lesson are you looking for?")
        print(course_name_search())
    elif islem_secimi==6:
        print("The transaction is being performed...")
        time.sleep(1)
        print(student_register())
    elif islem_secimi==7:
        print("The transaction is being performed...")
        time.sleep(1)
        print(crowded_class())
    elif islem_secimi==8:
        print("The transaction is being performed...")
        time.sleep(1)
        print("The exit was successful")
        break
    else:
        print("There is no such transaction")