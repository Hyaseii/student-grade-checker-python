def header() :
    print("="* 30)
    print("STUDENT GRADE CHECKER")
    print("="* 30)

def menu() :
    print("1. Cek Nilai Siswa ")
    print("2. Lihat Semua Nilai")
    print("3. Tambah Siswa")
    print("4. Hapus Nama Siswa")
    print("5. Perbarui Nilai")
    print("6. Statistika Nilai")
    print("7. Keluar")
    print()

def status_check(grade):
    if grade >= 75:
        return "Lulus"
    else :
        return "Tidak Lulus"

def calculate_average(grades) :
    total = sum(grades)
    amount = len(grades)
    return total / amount

def get_statistic(grades):
    amount = len(grades)
    minimum = min(grades)
    maximum = max(grades)
    total = sum(grades)
    average = total /amount

    return amount, minimum, maximum, average


student_grade = {
    "andi" : 80, 
    "budi" : 65,
    "caca" : 90,
    "dani" : 70
}

program_running = True
while program_running :
    header()
    menu()
    try : 
        unit = int(input("Pilih Menu : "))
        if unit == 1 :
            student_name = input("Masukan Nama Siswa: ")
            student_name = student_name.strip().lower()
            if student_name in student_grade : 
                grade = student_grade[student_name]
                status = status_check(grade)
                print("Nama : ",student_name)
                print("Nilai : ",grade)
                print("Status : ",status)
                print()
            else :
                print(f"Siswa bernama {student_name} tidak ditemukan di dalam daftar nilai.")

        elif unit == 2:
            for name,student_grade_2 in student_grade.items() :
                status = status_check(student_grade_2)
                print(name,":",student_grade_2," -",status)
            print()

        elif unit == 3:
            name = input("Masukan Nama Siswa : ")
            name = name.strip().lower()
            if name in student_grade :
                print(f"Siswa bernama {name} sudah tertera di dalam daftar nilai.")
            else :    
                name_check = name.replace(" ", "")
                if name_check.isalpha() :
                    print(name)
                    print("Nama Valid")
                    try :
                        grade = int(input("Masukan Nilai : "))
                        if grade > 100 :
                            print("Nilai tidak boleh lebih dari 100!")
                            print()
                        elif grade < 0 :
                            print("Nilai tidak boleh kurang dari 0!")
                            print()
                        else :     
                            student_grade[name] = grade
                    except ValueError:
                        print("Nilai harus berupa angka!!")
                else :
                    print(name)
                    print("Nama Tidak Valid")

        elif unit == 4 :
            del_name = input("Masukan Nama Siswa yang ingin dihapus : ")
            del_name = del_name.strip().lower()
            if del_name in student_grade :
                del student_grade[del_name]
                print(f"Siswa bernama {del_name} telah dihapus dari daftar nilai.")
                print()
            else : 
                print(f"Siswa bernama {del_name} tidak ditemukan di dalam daftar nilai.")
                print()

        elif unit == 5 :
            update_name = input("Masukan nama siswa : ")
            update_name = update_name.strip().lower()
            if update_name in student_grade :
                try :
                    update_grade = int(input("Masukan nilai terbaru : "))
                    if update_grade > 100 :
                        print("Nilai tidak boleh lebih dari 100!")
                        print()
                    elif update_grade < 0 :
                        print("Nilai tidak boleh kurang dari 0!")
                        print()
                    else : 
                        student_grade[update_name] = update_grade
                        print("Nilai berhasil diperbarui.")
                        print()
                except ValueError :
                    print("Nilai harus berupa angka!")
            else :
                print(f"Siswa bernama {update_name} tidak ditemukan.")

        elif unit == 6:
            print("---STATISTIKA NILAi---")
            
            student_amount, minimum, maximum, average = get_statistic(student_grade.values())

            print("Jumlah Siswa = ",student_amount)
            print("Nilai Tertinggi = ",maximum)
            print("Nilai Terendah : ",minimum)
            print("Rata - rata nilai : ", average)             

        elif unit == 7:
            print("Terimakasih telah menggunakan Student Grade Checker. ")
            program_running = False

        else :
            print("Pilihan Tidak Valid")

    except ValueError :
        print("Pilihan harus berupa angka!")