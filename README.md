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

## Thực hành Lab02
## Hướng dẫn cài đặt môi trường và cách chạy code
Download và đăng nhập vào Docker Desktop.
Mở Terminal tại thư mục chỉ định.
# **Chuẩn bị trên Server:**
1. **Cài đặt Docker:** Server cần được cài đặt Docker Engine.

2. **Cài đặt Docker Compose:** Docker Compose cũng cần được cài đặt trên server.

3. **Truy cập Server:** Truy cập vào server thông qua SSH hoặc một phương thức khác.

4. **Chuẩn bị file**
*Clone repository*
```sh
git clone https://github.com/RhzKisSa/cs317-lab2.git
```
*Download pre-trained model:*
Download pre-trained model at ([here](https://drive.google.com/file/d/1TWeVaNwtrFZxZWeYka_jda4eQgUXxxXm/view?usp=sharing))
Lưu ý model và các file sau khi clone phải ở cùng một thư mục.
Nén các file ... vào lab2.zip.
Mở Terminal tại thư mục chứa lab2.zip.

5. **Đưa Dự án lên Server:**
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
**Đưa các file vào một thư mục để dễ dàng quản lý**
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
6. **Chạy Docker Compose**
Tại thư mục chưa file *docker-compose.yml* chạy với lệnh:
```sh
docker-compose up --build -d
```
7. **Sử dụng phương thức predict để dự đoán**
Mở WSL và gõ lệnh
```sh
curl -X POST -F "file=@/duong_dan_den_file_anh_cua_ban/ten_file_anh.jpg" http://192.168.28.38:8000/predict/
```
ví dụ ảnh của tôi được lưu tại đường dẫn *D:/download/test.png* thì câu lệnh là:
```sh
curl -X POST -F "file=@/mnt/d/download/test.png" http://192.168.28.38:8000/predict/
```


8. **Push image lên Docker Hub**

- Đăng nhập vào Docker Hub
```sh
docker login
```
- Tag image (Gắn thẻ cho image):
```sh
docker tag your_model_api:latest your_dockerhub_username/my-model-api:latest
```
- Push image lên Docker Hub:
```sh
docker push your_dockerhub_username/your-model-api:latest
```
## Video demo:

[Link Video](https://drive.google.com/file/d/1H-MN06vPVRhEIJXcoFqHuogzYoibgeR7/view?usp=sharing)
