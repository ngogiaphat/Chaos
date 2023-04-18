# Chương II: Thuật toán

---

Có thể nói toán học là nền tảng của mọi chuyên ngành nghiên cứu khoa học tự nhiên và xã hội. So với các chuyên ngành kỹ thuật khác thì lịch sử ra đời và phát triển của công nghệ thông tin (CNTT) vẫn còn non trẻ. Tuy nhiên, cho đến thời điểm hiện tại, CNTT đã và đang phát triển nhanh chóng, vượt trội hơn hẳn so với các chuyên ngành khác cả về tốc độ, sản phẩm, mức độ ứng dụng và tính phổ biến của nó đối với tất cả mọi người trong mọi lĩnh vực.

Để đáp ứng các nhu cầu từ xây dựng các mô hình toán học cho xử lý, lưu trữ, khai thác và sử dụng dữ liệu, thông tin trong các ngành nghề, cho đến xây dựng các chương trình mày tính để trợ giúp con người trong công việc, học tập, nghiên cứu khoa học, v.v.. thì toán học là công cụ không thể thiếu được.

1. Khái niệm.
    
    Thuật toán hay giải thuật (tiếng anh là Algorithm) hay còn gọi là Giải thuật là 1 khái niệm của Toán học và Tin học. Bạn có thể đọc ở nhiều nguồn để hiểu thêm về nó. Cá nhân tôi định nghĩa dễ hiểu rằng, thuật toán là “thuật” (phương pháp) để giải quyết 1 bài toán. Nói dễ hiểu hơn, mỗi một bài toán giống như một chiếc hòm chứa đựng kho báu (kết quả, đáp án), và chiếc chìa khoá để mở cái hòm đó chính là “giải thuật”. Nếu dùng sai chìa khoá, bạn vẫn có thể mở được hòm, nhưng mà sẽ mất nhiều thời gian, hoặc mở được hòm thì kho báu ở bên trong bị méo mó, không toàn vẹn. Sử dụng đúng chìa khoá, sẽ giúp bạn lấy được kho báu 1 cách dễ dàng, nhanh chóng. Tất nhiên mỗi chiếc hòm sẽ luôn cần loại chìa khoá khác nhau, giống như một bài toán luôn có những giải thuật xác định. Không có chiếc chìa khoá nào mở được tất cả các hòm, cũng như không có giải thuật nào giải được toàn bộ các bài toán.
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%20II%20Thua%CC%A3%CC%82t%20toa%CC%81n%2042a94d73279845f4bfd38f29aed17ec0/Untitled.png)
    
2. Vai trò của thuật toán.
    - *Ví dụ để thấy được tầm quan trọng của có thuật toán và không có thuật toán*
3. Các đặc trưng của thuật toán.
    
    -Các thuật toán có 1 số tính chất chung, đó là: 
    
    +**Đầu vào** (Input): Một thuật toán có các giá trị đầu vào từ một tập đã được chỉ rõ.
    
    +**Đầu ra**(Output)**:** Từ mỗi tập các giá trị đầu vào, thuật toán sẽ tạo ra các giá trị đầu ra. Các giá trị đầu ra chính là nghiệm của bài toán.
    
    +**Tính dừng:** Sau một số hữu hạn bước thuật toán phải dừng.
    
    +**Tính xác định:** Ở mỗi bước, các bước thao tác phải hết sức rõ ràng, không gây nên sự nhập nhằng. Nói rõ hơn, trong cùng một điều kiện hai bộ xử lý cùng thực hiện một bước của thuật toán phải cho những kết quả như nhau.
    
    +**Tính đúng đắn (hiệu quả):** Trước hết thuật toán cần đúng đắn, nghĩa là sau khi đưa dữ liệu vào thuật toán hoạt động và đưa ra kết quả như ý muốn.
    
    +**Tính phổ dụng:** Thuật toán có thể giải bất kỳ một bài toán nào trong lớp các bài toán. Cụ thể là thuật toán có thể có các đầu vào là các bộ dữ liệu khác nhau trong một miền xác định.
    
4. Biểu diễn thuật toán: bằng ngôn ngữ tự nhiên, mã giả, sơ đồ khối.
    
    Thuật toán là một tập hợp các hướng dẫn để giải quyết một vấn đề hoặc hoàn thành một nhiệm vụ. Mọi thiết bị máy tính đều sử dụng các thuật toán, giúp cắt giảm thời gian cần thiết để làm mọi việc theo cách thủ công. Các thuật toán có thể được thiết kế bằng cách sử dụng mã giả, lưu đồ và sơ đồ khối. Chúng được viết bằng cách sử dụng các câu lệnh và biểu thức.
    
    Ví dụ: Ta có thuật toán tính tổng hai số nguyên a, b.
    
    - Biểu diễn thuật toán bằng ngôn ngữ tự nhiên (natural language):
        
        – Đầu vào: 2 số nguyên a, b
        
        – Đẩu ra: Tổng của 2 số nguyên a, b.
        
        – Thuật toán:
        
        - **Bước 1**: Nhập giá trị của a, b.
        - **Bước 2**: Tính Tổng = a + b.
        - **Bước 3**: Thông báo kết quả Tổng
        - **Bước 4**: Kết thúc.
    - Biển diễn thuật toán bằng mã giả (pseudo-code):
    
    ```c
    If a = 0 Then
    Begin
    If b = 0 Then
    Xuất “Phương trình vô số nghiệm”
    Else
    Xuất “Phương trình vô nghiệm”
    End
    Else
    Xuất “Phương trình có nghiệm x = -b/a”
    ```
    
    - Biển diễn thuật toán bằng sơ đồ khối (flow chart):
        
        Lưu đồ được sử dụng để trình bày các bước giải quyết vấn đề qua các hình khối khác nhau.
        
        ### **Một số qui ước ký hiệu lưu đồ:**
        
        ![Untitled](Chu%CC%9Bo%CC%9Bng%20II%20Thua%CC%A3%CC%82t%20toa%CC%81n%2042a94d73279845f4bfd38f29aed17ec0/Untitled%201.png)
        
    
    **Chọn lựa điều kiện**: sử dụng hình thoi, bên trong chứa biểu thức điều kiện. Sử dụng thêm các nhãn: Đ/Đúng,Y/Yes hoặc S/Sai,N/No.
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%20II%20Thua%CC%A3%CC%82t%20toa%CC%81n%2042a94d73279845f4bfd38f29aed17ec0/Untitled%202.png)
    
    **Xử lý công việc:** sử dụng hình chữ nhật, bên trong chứa nội dung xử lý.
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%20II%20Thua%CC%A3%CC%82t%20toa%CC%81n%2042a94d73279845f4bfd38f29aed17ec0/Untitled%203.png)
    
    **Quá trình thực hiện các thao tác**: dùng mũi tên để nối các thao tác.
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%20II%20Thua%CC%A3%CC%82t%20toa%CC%81n%2042a94d73279845f4bfd38f29aed17ec0/Untitled%204.png)
    
    ***Ví dụ***: Sử dụng lưu đồ để biểu diễn thuật toán tính tổng hai số nguyên a, b.
    

![Untitled](Chu%CC%9Bo%CC%9Bng%20II%20Thua%CC%A3%CC%82t%20toa%CC%81n%2042a94d73279845f4bfd38f29aed17ec0/Untitled%205.png)

1. Một số ví dụ về thiết kế thuật toán.
    
    ### Thiết kế thuật toán là gì ?
    
    Thiết kế thuật toán đề cập đến 1 phương pháp hoặc 1 quy trình toán học để giải quyết vấn đềvấcc thuật toán kỹ thuật. Việc thiết các thuật toán là 1 phần của nhiều lý thuyết giải pháp nghiên cứu hoạt động, chẳng hạn như **lập trình năng động** và **chia để trị**. Các kỹ thuật thiết kế và triển khai các thiết kế thuật toán còn được gọi là các mẫu thiết kế thuật toán, với các ví dụ bao gồm mẫu phương pháp mẫu và mẫu trang trí.
    
    Một trong những khía cạnh quan trọng nhất của thiết kế thuật toán nằm ở việc tạo ra thuật toán có thời gian chạy hiệu quả, còn được gọi là **Big O** của nó.
    
    ### Các bước cơ bản trong quá trình phát triển thuật toán:
    
    1. Định nghĩa vấn đề
    2. Phát triển 1 mô hình 
    3. Đặc điểm kỹ thuật của thuật toán
    4. Thiết kế 1 thuật toán
    5. Kiểm tra **tính đúng đắn** của thuật toán
    6. Phân thích thuật toán
    7. Thực hiện thuật toán
    8. Chương trình thử nghiệm
    9. Viết tài liệu
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%20II%20Thua%CC%A3%CC%82t%20toa%CC%81n%2042a94d73279845f4bfd38f29aed17ec0/Untitled%206.png)
    
    ### Thực hiện:
    
    Hầu hết các thuật toán được thiết kế để thực hiện như các chương trình máy tính. Tuy nghiên, các thuật toán cũng được thực hiện bằng các phương tiện các, chẳng hạn như trong mạng nơ-ron sinh học (ví dụ: não người thực hiện phép tính số học hoặc côn trùng đang tìm kiếm thức ăn), trong mạch điện hoặc trong 1 thiết bị cơ khí.
    

***Chú thích:**

1. Lập trình năng động: Trong ngành Khoa học máy tính (tiếng Anh: Computer Science - SE), lập trình năng động (tiếng Anh: *dynamic programming*) là 1 phương pháp giảm thời gian chạy của các thuật toán thể hiện các tính chất của các bài toán con gối nhau *(overlapping subproblem)* và cấu trúc con tối ưu *(optimal subtructure)*
2. Chia để trị:  Trong ngành Khoa học máy tính, chia để trị là 1 mô hình thiết kế thuật toán quan trọng dựa trên đệ quy với nhiều phân nhánh. Thuật toán chia để trị hoạt động bằng cách chia bài toán thành nhiều bài toán nhỏ hơn thuộc cùng thể loại, cứ như vậy lặp lại nhiều lần, cho đến khi bài toán thu được đủ đơn giản để có thể giải quyết trực tiếp. Sau đó lời giải của các bài toán nhỏ được tổng hợp lại thành lời giải cho bài toán ban đầu.
3. Big O: Trong Toán học, ký hiệu O lớn dùng để chỉ hành vi giới hạn của 1 hàm số khi đối số tiến đến 1 giá trị nhất định hoặc vô cùng. Trong Khoa học máy tính, ký hiệu O lớn dùng để mô tả hành vi thuật toán (ví dụ: Về mặc thời gian hoặc lượng bộ nhớ cần dùng) khi kích thước dữ liệu thay đổi.
4. Tính đúng đắn: Sự phù hợp với tiêu chuẩn đã được thừa nhận hoặc được chấp nhận.