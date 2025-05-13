<!-- Banner -->
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<h1 align="center"><b>Information Retrieval</b></h1>

<div align="center">
  <table>
    <thead>
      <tr>
        <th>STT</th>
        <th>MSSV</th>
        <th>Họ và Tên</th>
        <th>Chức vụ</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>22520646</td>
        <td>Nguyễn Quốc Khánh</td>
        <td>Nhóm trưởng</td>
      </tr>
      <tr>
        <td>2</td>
        <td>22520775</td>
        <td>Nguyễn Xuân Linh</td>
        <td>Thành viên</td>
      </tr>
      <tr>
        <td>3</td>
        <td>22521677</td>
        <td>Nguyễn Thế Vĩnh</td>
        <td>Thành viên</td>
      </tr>
      <tr>
        <td>4</td>
        <td>22521671</td>
        <td>Lưu Khánh Vinh</td>
        <td>Thành viên</td>
      </tr>
    </tbody>
  </table>
</div>

# COURSE INTRODUCTION
* **Course Name:** MLOps - Phát triển và vận hành hệ thống máy học.
* **Class Code:** CS317.P21.
* **Academic Year:** HK2 (2024 - 2025).
* **Lecturer**: Th.S Đỗ Văn Tiến, Lê Trần Trọng Khiêm

# Thực hành Lab02
## Hướng dẫn cài đặt môi trường và cách chạy code
Download và đăng nhập vào Docker Desktop.
Mở Terminal tại thư mục chỉ định.
# **Chuẩn bị trên Server:**
1. Cài đặt Docker: Server của bạn cần được cài đặt Docker Engine.

2. Cài đặt Docker Compose: Docker Compose cũng cần được cài đặt trên server.

3. Truy cập Server:Truy cập vào server thông qua SSH hoặc một phương thức khác.

4. Chuẩn bị file
*Clone repository*
```sh
git clone https://github.com/RhzKisSa/cs317-lab2.git
```
*Download pre-trained model:*
Download pre-trained model at ([here](https://drive.google.com/file/d/1TWeVaNwtrFZxZWeYka_jda4eQgUXxxXm/view?usp=sharing))
Lưu ý model và các file sau khi clone phải ở cùng một thư mục.
Nén các file ... vào lab2.zip.
Mở Terminal tại thư mục chứa lab2.zip.

5. Đưa Dự án lên Server:
```sh
scp lab2.zip server_user@server_ip:/home/server_user/your_folder/
```
- Cài đặt unzip (nếu chưa có):
```sh
sudo apt update
```
```sh
sudo apt install unzip -y
```
- Giải nén file lab2.zip:
```sh
unzip lab2.zip
```
*Đưa các file vào một thư mục để dễ dàng quản lý*
- Tạo thư mục chứa file
```sh
mkdir your_folder_name
```
- Di chuyển các file vào thư mục
```sh
mv Dockerfile your_folder_name/
mv docker-compose.yml your_folder_name/
mv main.py your_folder_name/
mv model.pth your_folder_name/
mv my_model_definition.py your_folder_name/
mv requirements.txt your_folder_name/
```  
- Di chuyển đến thư mục mới
```sh
cd your_folder_name
```
6. Chạy Docker Compose
Tại thư mục chưa file *docker-compose.yml* chạy với lệnh:
```sh
docker-compose up --build -d
```



- Linux :


  - Nếu không cài được python 3.10 bạn có thể thử ([Link sau](https://stackoverflow.com/questions/75131112/how-to-install-python3-10-virtual-environment-when-python3-10-venv-has-no-instal))
- Window: có thể tải về máy ([tại đây](https://www.python.org/downloads/))
2. **Clone git**
- Đảm bảo đã tải git về máy ([tải tại đây](https://git-scm.com/downloads))
- Mở Folder để lưu dữ liệu được tải về, sau đó khởi tạo git

- Clone code về:
```sh
git clone git@github.com:NguyenQuocKhanh1301/CS317_Lab01.git
```
3. **Tạo môi trường ảo (venv or conda ...)**
- Chuyển qua file đã clone về
```sh
cd your_folder_name
```
- Mở terminal và khởi tạo môi trường ảo với venv:
  ```sh
  python3.10 -m venv venv
  ```
- Activate môi trường ảo
  - Linux
  ```sh
  source venv/bin/activate
  ```
  - Window
 ```sh
.\venv\Scripts\activate
 ```
4. **Cài đặt thư viện**

Cài đặt các thư viện cần thiết:
```sh
pip install --upgrade pip
```
```sh
pip install -r requirements.txt
```
5. **Mở giao diện mlflow**

Sử dụng lệnh sau để ui của mlflow với
- host: 0.0.0.0 
- port: 5003
```sh
mlflow ui --host 0.0.0.0 --port 5003
```
6. **Run pipeline**

Để chạy pipeline training sử dụng câu lệnh sau:
```sh
python lab01.py
```
7. **Load model và đánh giá**

Sau khi chon được model tốt nhất thì tiến hành đánh giá:
```ssh
python Evaluation.py
```
## Video demo:

[Link Video](https://drive.google.com/file/d/1H-MN06vPVRhEIJXcoFqHuogzYoibgeR7/view?usp=sharing)
