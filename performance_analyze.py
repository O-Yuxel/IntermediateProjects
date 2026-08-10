import numpy as np

grades = np.array([
    [78, 85, 92, 67, 88],
    [91, 73, 84, 95, 79],
    [65, 89, 76, 82, 70],
    [88, 94, 91, 87, 96],
    [72, 68, 75, 81, 77],
    [95, 90, 88, 92, 85],
    [59, 64, 71, 68, 73],
    [84, 79, 93, 86, 90]
])

print("----------PART 1----------")

total_student = np.shape(grades)[0]
total_lesson = np.shape(grades)[1]
mean_notes = np.mean(grades)
max_note = np.max(grades)
min_note = np.min(grades)
deviation_all_notes = np.std(grades)

print("Öğrenci sayısı: ", total_student)
print("Ders sayısı: ", total_lesson)
print("Bütün notların ortalaması: ", mean_notes)
print("En yüksek not: ", max_note)
print("En düşük not: ",min_note)
print("Bütün notların standart sapması: ", deviation_all_notes)


print("\n----------PART 2----------")

students = ["Öğrenci 1", "Öğrenci 2", "Öğrenci 3", "Öğrenci 4", "Öğrenci 5", "Öğrenci 6", "Öğrenci 7", "Öğrenci 8"]

students_mean = np.mean(grades, axis=1)
best_mean = np.max(students_mean)
best_student = np.argmax(students_mean)
worst_student = np.argmin(students_mean)
worst_mean = np.min(students_mean)
print(f"En iyi öğrenci {students[best_student]}'dir. Not ortalaması da {best_mean}'dir.")
print(f"En kötü öğrenci {students[worst_student]}'dir. Not ortalaması da {worst_mean}'dir.")


print("\n----------PART 3----------")

lessons = ["Matematik", "Edebiyat", "Biyoloji", "Fizik", "Tarih"]

lessons_mean = np.mean(grades, axis=0)
lessons_deviation = np.std(grades, axis=0)
best_lesson = np.argmax(lessons_mean)
worst_lesson = np.argmin(lessons_mean)
print(f"Ortalaması en yüksek ders {lessons[best_lesson]}'dır. Ortalaması en düşük ders {lessons[worst_lesson]}.")
print("\nDerslerin standart sapması: ")
n = 0
for i in lessons_deviation:
    print(lessons[n], ":", i)
    n += 1


print("\n----------PART 4----------")

mask = np.mean(grades, axis=1) < 70
student_array = np.array(students)
print("Başarısız öğrenciler:", student_array[mask], "ve not ortalamaları:", students_mean[mask])


print("\n----------PART 5----------")

succesful_students = np.all(grades >= 80, axis=1)
print("Başarılı öğrenciler: ",student_array[succesful_students])


print("\n----------PART 6----------")

grades_plus5 = grades + 5
grades_clipped = np.clip(grades_plus5,0,100)
print(grades_clipped)


print("\n----------PART 7----------")

critic_students = np.sum(grades < 60, axis=1) >= 3
print("Kritik durumda olan öğrenciler şunlardır: ",student_array[critic_students])


print("\n----------PART 8----------")

students_sorted = np.argsort(students_mean)[::-1]
print("En başarılıdan ne başarısız öğrenciye olan sıralama: ")
for i in students_sorted:
    print(students[i], end=" ")