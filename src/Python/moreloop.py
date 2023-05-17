students = []
while True:
    info = input("Nhập tên, điểm môn tin và ngày sinh của bạn (cách nhau bởi dấu phẩy): ")
    if not info:
        break
    student = info.split(",")
    students.append(student)
print("Danh sách sinh viên:")
for student in students:
    print("Tên: ", student[0], ", Điểm tin: ", student[1], ", Ngày sinh: ", student[2])