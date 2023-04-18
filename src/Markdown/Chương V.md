## **1/ Giới thiệu về vòng lặp:**

### 1.1: Thế nào là vòng lặp:

Vòng lặp (hay Loop) là thuật ngữ để chỉ một hành động hoặc cụm hành động lặp đi lặp lại nhiều lần. Trong quá trình coding, có những khi chúng ta muốn chạy đi chạy lại một câu code nhiều lần. Đó là lúc bạn cần đến vòng lặp.

### 1.2: Tình huống sự dụng vòng lặp:

- In các số từ 1 - 10
- Tính tổng từ 1- 10
- Kiểm tra điều kiện nhập

Đây là một số trường hợp phổ biến cần sử dụng vòng lặp, và còn nhiều tình huống sử dụng vòng lặp phứt tạp hơn

## **2/ Cấu trúc vòng lặp for, while, do-while:**

### 2.1: Cấu trúc vòng lặp for:

```c
for (khởi tạo; điều kiện; lặp) {
// nội dung của vòng lặp 'for'
}

//in 10 số nguyên đầu tiên
for(int i = 0; i < 10; i++) {
	printf("%d\n", i);
}
```

### 2.2: Cấu trúc vòng lặp while:

```c
while (điều kiện) {
// nội dung của vòng lặp
}

//tính tổng 10 số nguyên đầu tiên
int i = 1, tong = 0;
while(i <= 10) {
	tong += i;
	i++;
}
//nhớ chú ý giá trị khởi tạo chứ không nó sẽ thành vòng lặp vô hạn đấy nhé!!!
```

### 2.3: Cấu trúc vòng lặp do-while:

```c
do {

} while(điều kiện);

//nhập số nguyên n thõa điều kiện 10 <= n <= 20
do {
	scanf("%d",&n);
} while(n < 10 || n > 20);
```

## 3: So sánh các vòng lặp

[3.1: So sánh for và while : (1)](https://www.notion.so/d0c05f6e29a749b2a470b962308c5344)

[3.2: So sánh while và do-while: (1)](https://www.notion.so/e7f9adb01cc84f65b87bb7a62b0995f6)

## 4: Break và continue:

### 4.1:Break

Break dùng để kết thúc vòng lặp và thoát khỏi vòng lặp.

4.1.1: Cách hoạt động của lệnh break:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9466ac47-c6a9-4c74-852b-1899e8635f8d/Untitled.png)

4.1.2: Ví dụ về break:

```c
//Kiểm tra một số nguyên mà nó được tạo thành từ các số chẵn hay không
#include <stdio.h>
 
int main(){
    int number;
    printf("\nNhap number = ");
    scanf("%d", &number);
 
    bool allEven = true; // Giả sử ban đầu là đúng
    int last;
    while(number > 0){
        last = number % 10; // lấy c/số cuối của number
 
        if(last % 2 == 1){
            allEven = false;
            break; // thoát vòng lặp
        }
        number /= 10; // bỏ chữ số cuối của number
    }

    if(allEven){
        printf("\nToan chu so chan!");
    }else{
        printf("\nCo chu so le!");
    }
}
```

4.2: Continue:

Continue dùng kết thúc sớm một vòng lặp và tiếp tục vòng lặp tiếp theo.

4.2.1: Cách hoạt động của continue:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dee79cee-8aed-45c8-af6a-9b49e72dc335/Untitled.png)

4.2.2: Ví dụ về continue:

```c
//In ra các chữ số chẵn từ 1 đến 100.
#include <stdio.h>
 
int main(){
    for(int i = 0; i <= 100; i++){
        if(i % 2 != 0){
            continue;
        }
        printf("%d ", i);
    }
}
```