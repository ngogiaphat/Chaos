while True:
    name = input("Nhập tên của bạn: ")
    diem = input("Nhập điểm môn tin của bạn: ")
    ngaysinh = input("Nhập ngày sinh của bạn: ")
    print("Tên: ", name)
    print("Điểm môn tin: ", diem)
    print("Ngày sinh: ", ngaysinh)
    tieptuc = input("Bạn có muốn nhập tiếp không? (Y/N)")
    if tieptuc.lower() == "n":
        break