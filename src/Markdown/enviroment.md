# CHƯƠNG 1: CÀI ĐẶT MÔI TRƯỜNG C, C++, PYTHON TRÊN WINDOWS, LINUX


## *TẠO MÔI TRƯỜNG C, C++, PYTHON TRÊN WINDOWS*

# 1. Cài đặt môi trường C/C++

### ***Cài đặt IDE để biên dịch và thực thi C/C++***

Để biên dịch và thực thi chương trình [C](https://quantrimang.com/lap-trinh-c%20), bạn cần sử dụng một **IDE  (Integrated Development Environment)**  như **Dev-C++, Code:: Blocks, VScode** hoặc **Turbo C.** 

- Link để tải Dev C++: [https://sourceforge.net/projects/orwelldevcpp/](https://sourceforge.net/projects/orwelldevcpp/)
- Link để tải Code::Blocks : [https://sourceforge.net/projects/codeblocks/](https://sourceforge.net/projects/codeblocks/)

Sau khi tải xong, hãy làm theo [hướng dẫn cài đặt Dev C++](([https://thaomy-18.notion.site/IDE-v-editor-tr-n-Windown-608a81fefbfd4a3d86a048346ad79686](https://www.notion.so/IDE-v-editor-tr-n-Windown-608a81fefbfd4a3d86a048346ad79686))  để biên dịch và thực thi C/C++.

### ****Cài đặt để chạy trên Command Prompt****

Nếu bạn đang muốn cài đặt chương trình C, bạn cần phải sử dụng 2 phần mềm trên máy tính của bạn: 

***a) Chương trình soạn văn bản - Text Editor*** 

Text editor được sử dụng để soạn thảo các chương trình. Ví dụ về một vài trình editor như Window Notepad, Notepad ++,...

Các file bạn tạo trong trình editor được gọi là source file (file nguồn) và chứa các chương trình code. Các file trong chương trình C thường được đặt tên với phần mở rộng ".c" và “.cpp” trong chương trình C+++.

***b) Bộ biên dịch - C/C++ Compiler***

Mã nguồn được viết trong file nguồn dưới dạng ngôn ngữ bậc cao. Để cho CPU có thể thực hiện các chương trình này thì các lệnh được viết trong file sẽ được biên dịch thành ngôn ngữ máy thông qua **bộ biên dịch C/C++.** 

Bộ biên dịch thông dụng nhất là bộ biên dịch GNU C/C++, mặt khác bạn có thể có các bộ biên dịch khác như HP hoặc Solaris với Hệ điều hành tương ứng.

**Cài đặt GNU C/C++ trên Windows*

Để cài đặt GCC trên Windows bạn cần phải cài đặt MinGW. Để cài đặt MinGW, bạn truy cập vào <[https://codecute.com/c/huong-dan-cai-dat-trinh-bien-dich-c-c-mingw-gcc.html](https://codecute.com/c/huong-dan-cai-dat-trinh-bien-dich-c-c-mingw-gcc.html)> và theo hướng dẫn trên trang này.

Trong quá trình cài đặt MinWG, ít nhất bạn phải cài đặt gcc-core, gcc-g++, binutils và MinGW runtime (có thể cài đặt nhiều hơn)

Thêm thư mục con bin trong nơi cài đặt MinGW vào biến môi trường **PATH** của bạn để có thể sử dụng trực tiếp các công cụ dưới dạng command line một các dễ dàng.\

Khi quá trình cài đặt hoàn tất, bạn có thể chạy gcc, g++, ar, ranlib, dlltool và các công cụ GNU khác trên Windows command line.

# 2. Cài đặt môi trường Python

**Có rất nhiều cách để chúng ta có thể chạy ngôn ngữ Python. Và một trong số cách thuận tiện nhất đó chính là chạy python trên cmd (Windows Terminal) và có tên chính xác là *Windows Prompt*.**

**Tuy nhiên để có thể chạy python trên cmd, bạn cần phải khai báo vị trí cài đặt của python trong máy của bạn cho hệ điều hành biết, hay nói cách khác là cài đặt môi trường python trên hệ điều hành.Bạn có thể làm được điều này bằng cách tích vào *Add_Python to PATH* khi cài đặt Python.**

**Tuy nhiên nếu bạn quên không tích option ở trên khi cài Python thì cũng đừng lo lắng, chúng ta cũng có thể cài đặt môi trường Python ngay cả sau khi cài nó đơn giản bằng cách thêm Python vào biến môi trường Windows PATH.**



- Xem hướng dẫn cài đặt và khởi động Python theo cách cổ điển tại <[https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/cai-dat-python/thiet-lap-moi-truong-trong-python/#Cai-dat-moi-truong-python-cho-Anaconda-Python](https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/cai-dat-python/thiet-lap-moi-truong-trong-python/#Cai-dat-moi-truong-python-cho-Anaconda-Python)>
- Cách cài đặt môi trường python cho Anaconda Python cũng tương tự cách cổ điển. Có điều là thay vì chỉ thêm đường dẫn của Python, lần này bạn sẽ cần phải thêm cả đường dẫn Python lẫn của Anaconda mà chúng ta đã tìm ở [trên](https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/cai-dat-python/thiet-lap-moi-truong-trong-python/#Khi-ban-da-cai-Anaconda-Python) vào biến môi trường PATH Windows.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3457117-8710-4007-b775-abb40f6033cb/Untitled.png)

# *TẠO MÔI TRƯỜNG C, C++, PYTHON TRÊN LINUX*

## 1. Cài đặt môi trường C/C++

***Cài đặt chạy trên Terminal***

Đầu tiên, mã chương trình C được biên dịch bởi một trình biên dịch để chuyển mã dựa trên chuỗi thành mã máy mà máy tính có thể đọc được. Trong ***Linux***, trình biên dịch phổ biến nhất được sử dụng để lập trình C là trình biên dịch GCC và có sẵn trong kho lưu trữ mặc định của nhiều bản phân phối Linux có thể được cài đặt dễ dàng bằng trình quản lý gói ***apt***:

Mã Nguồn:

<aside>
💡 sudo apt install gcc

</aside>

![Screenshot 2022-04-20 233036.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9c903a23-0424-4a32-9b95-1a5447a78737/Screenshot_2022-04-20_233036.png)

Sau khi gói GCC đã được cài đặt, bây giờ là lúc tạo tập tin bằng trình soạn thảo ***nano*** với tên ***test.c*** , ("***.c***" là phần mở rộng cho máy tính biết rằng tập tin này chứa chương trình C, và “***.cpp***” là phần mở rộng cho máy tính biết rằng tập tin này chứa chương trình C++):

Mã Nguồn:

<aside>
💡 nano test.c

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2fb23128-16d4-4442-a63f-6032e9a3f7df/Untitled.png)

Một ít code in ra ***“Hello World!”***:

```c
#include<stdio.h>
											//Welcome to IUH Coder
int main()
{
			printf("Hello World!");
}
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/104e35c8-0c5e-4e52-a8e2-6e753cadfa2f/Untitled.png)

Nhấn ***`CTRL + S`*** để lưu tập tin và thoát khỏi trình soạn thảo bằng cách nhấn ***`CTRL + X`***. Liệt kê tên của các tập tin bằng cách sử dụng lệnh `ls` để kiểm tra việc tạo tập tin đã hoàn tất chưa.

Mã Nguồn:

<aside>
💡 ls

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a2b49c30-888b-4c99-ae33-0f76ef79a2dd/Untitled.png)

Xác nhận tập tin đã tạo thành công. Để biên dịch tập tin bằng trình biên dịch ***GCC*** hãy nhập lệnh như sau:

<aside>
💡 gcc test.c -o test

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/774cb82d-c24e-485a-a625-65e6c9bc52c5/Untitled.png)

Trong lệnh trên, ***GCC*** là trình biên dịch, biên dịch tập tin được tạo với tên *test.c* và sau đó kiểm tra xem nó có lỗi hay không và nếu không có lỗi, thì *"test"* (tập tin nhị phân) sẽ được tạo trong cùng một thư mục.

Để thực thi tập tin, hãy sử dụng:

Mã Nguồn:

<aside>
💡 ./test

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63435500-5f8c-4678-96d5-84a62e171ab2/Untitled.png)

Trong kết quả đầu ra ở trên, chúng ta đã thấy rằng kết quả đầu ra của chương trình C của chúng ta đã được hiển thị như mong muốn.

## 2. Cài đặt môi trường PYTHON

Đây là cách đơn giản nhất, các bạn không cần phải lên trang chủ ***python*** để tải *file, giải nén…*

Đầu tiên sử dụng lệnh:

Mã Nguồn:

<aside>
💡 sudo apt-get update

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d3bfdf16-739f-40b2-ae4b-0917e23cb9ff/Untitled.png)

Sau đó, sử dụng lệnh tiếp theo:

Mã Nguồn:

<aside>
💡 sudo apt-get install python

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c980093d-4ed7-4112-8e78-eec3c50fa8c0/Untitled.png)

Mặc định nó sẽ cài cho bạn 2 bản ***python*** là ***2.x*** và ***3.x***

Để kiểm tra ***version*** của ***python*** sau khi cài đặt các bạn dùng lệnh sau:

> Đối với ***python*** bản 2.x sử dụng câu lệnh: `python` hoặc là `python -V`
> 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bcb8097e-a7b8-453e-9b9a-69604f9e79d2/Untitled.png)

> Đối với python bản 3.x sử dụng câu lệnh:  `python`  hoặc là  `python3 -V`
> 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/addce08d-e4c3-444d-bcfa-e61feabf4f7e/Untitled.png)

Một ít code in ra ***“Hello IUHCoder”***:

```c
print("***Hello IUHCoder")***
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fa435aac-733d-46f8-89c1-3efa7e01da19/Untitled.png)

Nếu bạn muốn thoát khỏi trình biên dịch. Hãy nhấn `CTRL + Z`  để thoát nhé.

### Cài đặt pip cho PYTHON

pip (***python package manager***) là một trình quản lý ***module***, thư viện của ***python***.

> Đối với python:
> 

<aside>
💡 sudo apt-get install pip

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a0aa360-736e-4adf-b8cd-ff2b5b8f5be6/Untitled.png)

> Đối với python3:
> 

<aside>
💡 sudo apt-get install pip3

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1978e719-0e05-4b7a-bb94-ec8d083e4f97/Untitled.png)

Ví dụ bạn muốn thực hiện kết nối tới database bằng python thì bạn phải có module mysqlclient (trong java thì là thư viện jdbc). Nhưng khi cài python nó chưa có sẵn module đó, để cài module mysqlclient ta cài qua pip bằng lệnh **`pip install mysqlclient`**