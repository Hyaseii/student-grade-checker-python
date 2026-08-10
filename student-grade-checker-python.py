def header() :
    print("="* 30)
    print("STUDENT GRADE CHECKER")
    print("="* 30)

def menu() :
    print("1. Cek Nilai Siswa ")
    print("2. Lihat Semua Nilai")
    print("3. Keluar")

def status_check(grade) :
    if grade >= 75 :
        return("Lulus")
    else :
        return("Tidak Lulus")

student_grade = {
    "Andi" : 80, 
    "Budi" : 65,
    "Caca" : 90,
    "Dani" : 70
}

program_running = True
while program_running :
    header()
    menu()
    unit = int(input("Pilih Menu : "))
        
    if unit == 1 :
        student_name = input("Masukan Nama Siswa: ")
        if student_name in student_grade : 
            grade = student_grade[student_name]
            status = status_check(grade)
            print("Nama : ",student_name)
            print("Nilai : ",grade)
            print("Status : ",status)
            print()
        else :
            print("Nama Siswa tidak ditemukan.")

    elif unit == 2:
        for name,student_grade_2 in student_grade.items() :
            status = status_check(student_grade_2)
            print(name,":",student_grade_2," - ",status)
        print()

    elif unit == 3:
        print("Terimakasih telah menggunakan Student Grade Checker. ")
        program_running = False

    else :
        print("Pilihan Tidak Valid")