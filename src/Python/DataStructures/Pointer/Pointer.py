# Khởi tạo một đối tượng a kiểu int với giá trị là 10
a = 10
# Khai báo một con trỏ b trỏ tới đối tượng a
b = id(a)
# In giá trị của a và b
print("Giá trị của a là:", a)
print("Địa chỉ của a là:", hex(id(a)))
print("Giá trị của b là:", b)
print("Địa chỉ của b là:", hex(id(b)))
# Thay đổi giá trị của a
a = 20
# In giá trị của a và b sau khi thay đổi giá trị của a
print("Sau khi thay đổi giá trị của a:")
print("Giá trị của a là:", a)
print("Địa chỉ của a là:", hex(id(a)))
print("Giá trị của b là:", b)
print("Địa chỉ của b là:", hex(id(b)))
