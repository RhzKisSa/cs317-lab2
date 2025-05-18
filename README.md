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
1. **Chuẩn bị trên Server:**
- **Cài đặt Docker:** Server cần được cài đặt Docker Engine.

- **Cài đặt Docker Compose:** Docker Compose cũng cần được cài đặt trên server.

- **Truy cập Server:** Truy cập vào server thông qua SSH hoặc một phương thức khác.

2. **Chuẩn bị file:**
*Clone repository*
```sh
git clone git@github.com:RhzKisSa/cs317-lab2.git
```
*Download pre-trained model:*
Download pre-trained model at ([here](https://drive.google.com/file/d/1TWeVaNwtrFZxZWeYka_jda4eQgUXxxXm/view?usp=sharing))
Lưu ý model và các file sau khi clone phải ở cùng một thư mục.

3. **Build image trên local:**
- Mở Terminal tại thư mục chứa cs317-lab02 (đã clone)
```sh
docker build -t yourdockerhubusername/lab02:latest service-api 
```
- Push image lên Docker Hub:
```sh
docker login
docker push yourdockerhubusername/lab02:latest
```
4. **Deploy Docker Compose:**
- Di chuyển file *docker-compose.yml* lên server:
```sh
scp docker-compose.yml server_user@server_ip:/home/server_user/your_folder/
```
- Mở terminal trên server chuyển đến folder chứa file *docker-compose.yml*
```sh
cd /home/server_user/your_folder
```
- Pull Docker image đã push lên Docker Hub:
```sh
docker-compose pull
```
- Thực hiện run container:
```sh
docker-compose up -d --build
```
5. **Sử dụng phương thức predict để dự đoán:**
Mở WSL ở local và gõ lệnh
```sh
curl -X POST -F "file=@/duong_dan_den_file_anh_cua_ban/ten_file_anh.jpg" http://192.168.28.38:8000/predict/
```
ví dụ ảnh của tôi được lưu tại đường dẫn *D:/download/test.png* thì câu lệnh là:
```sh
curl -X POST -F "file=@/mnt/d/download/test.png" http://192.168.28.38:8000/predict/
```

7. ## Video demo:

[Link Video](https://drive.google.com/file/d/1DJ9JjSqxwKapUK1miyIhpDYmi2py5kIC/view)
