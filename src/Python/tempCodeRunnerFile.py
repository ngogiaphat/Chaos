#Tạo 1 mảng rỗng để chứa danh sách học sinh
students = []
#Lặp
while True:
    name = input("Nhập tên học sinh (nhập 's' để kết thúc): ")
    #Nếu nhập 's' thì dừng vòng lặp và in ra danh sách học sinh
    if name == 's':
        break
    #Nhập input
    tin = float(input("Nhập điểm tin: "))
    dob = input("Nhập ngày sinh (dd/mm/yyyy): ")
    students.append({'ten': name, 'tin': tin, 'dob': dob})
#In ra danh sách học sinh
print("Danh sách học sinh:")
for student in students:
    print("Tên:", student['ten'], "Điểm tin:", student['tin'], "Ngày sinh:", student['dob'])