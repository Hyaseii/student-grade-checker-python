# Student Grade Checker

A simple Python console application for managing and checking student grades.

This project was created as a learning project to practice Python fundamentals, especially functions, dictionaries, input validation, loops, and error handling.

## Features

- Check a student's grade
- View all student grades
- Add a new student
- Update a student's grade
- Delete a student
- Automatically determine whether a student passes or fails
- Prevent duplicate student names
- Validate student names
- Validate grades between 0 and 100
- Handle invalid numeric input
- Case-insensitive student name input
- grade statistics
- average grade calculation
- highest grade detection
- lowest grade detection

## Concepts Used

This project uses several basic Python concepts:

- Variables
- Input and output
- `if`, `elif`, and `else`
- `while` loop
- `for` loop
- Functions
- Parameters and arguments
- `return`
- Dictionary
- Dictionary methods
- `in` operator
- `del`
- `.strip()`
- `.lower()`
- `.replace()`
- `.isalpha()`
- `try / except`
- `ValueError`
- Input validation
- max()
- min()
- len()
- sum()

# Menu

```text
==============================
STUDENT GRADE CHECKER
==============================

1. Cek Nilai Siswa
2. Lihat Semua Nilai
3. Tambah Siswa
4. Hapus Nama Siswa
5. Perbarui Nilai
8. Statistik Nilai
7. Keluar

## Example 

Masukan Nama Siswa: Budi

Nama : budi
Nilai : 65
Status : Tidak Lulus

## Adding a Student

Masukan Nama Siswa : Eko
Nama Valid
Masukan Nilai : 85

## Invalid Grade 

Masukan Nilai : 120
Nilai tidak boleh lebih dari 100!

## Duplicate Student

Masukan Nama Siswa : Budi
Siswa bernama budi sudah tertera di dalam daftar nilai.

## Student Not Found

Masukan nama siswa : Zaki
Siswa bernama zaki tidak ditemukan.

## Statistik Grade

---STATISTIKA NILAi---
Jumlah Siswa =  4
Nilai Tertinggi =  90
Nilai Terendah :  65
Rata - rata nilai :  76.25

## Version

Version 1.3

Changelog

Version 1.3
- Added grade statistics
- Added average grade calculation
- Added highest grade detection
- Added lowest grade detection

Version 1.2
- Added student grade update feature
- Added grade validation for updated grades
- Improved student grade management

Version 1.1
- Added student creation
- Added student deletion
- Added student name validation
- Added grade validation
- Added duplicate student detection
- Added case-insensitive name handling
- Improved input error handling
- Improved program structure using functions

Version 1.0
- Added student grade checking
- Added view all student grades
- Added pass/fail status checking
- Added basic menu system
- Future Improvements

## Possible features for future versions:

Update student grades
Search students more efficiently
Calculate average grade
Show the highest and lowest grades
Save student data to a file
Load student data when the program starts
Improve the user interface

## bash

python student_grade_checker.py

## Author

Hyaseii
