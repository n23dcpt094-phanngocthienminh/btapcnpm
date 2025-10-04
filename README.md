# 🏨 Hệ Thống Quản Lý Đặt Phòng Khách Sạn

## 📝 Giới thiệu
**Mini App Hotel Booking** là một hệ thống hỗ trợ khách hàng đặt phòng khách sạn trực tuyến, giúp tối ưu quy trình tìm kiếm, đặt phòng và thanh toán.  
Người dùng có thể:
- Xem danh sách phòng theo loại, giá, tiện nghi.  
- Đặt phòng trực tuyến và thanh toán nhanh chóng.  
- Quản lý lịch sử đặt phòng, hủy phòng, đánh giá khách sạn.  

Hệ thống được phát triển nhằm hỗ trợ **khách hàng**, **lễ tân** và **quản lý khách sạn** trong việc vận hành, theo dõi và tối ưu hiệu quả dịch vụ.

---

## 👥 Thành viên nhóm
- Phan Ngọc Thiên Minh -Leader
- Nguyễn Ngọc Bảo Linh
- Lê Minh Khang
---

## 🚀 Chức năng chính
### 👤 Khách hàng
- Đăng ký/đăng nhập tài khoản  
- Tìm kiếm, xem thông tin phòng (giá, loại, tiện nghi)  
- Đặt phòng và thanh toán trực tuyến  
- Xem lịch sử đặt phòng, hủy hoặc đánh giá  

### 🏢 Nhân viên lễ tân
- Quản lý thông tin khách hàng  
- Xác nhận, cập nhật tình trạng phòng  
- Hỗ trợ hủy phòng, hoàn tiền  

### 🧑‍💼 Quản lý
- Quản lý danh sách phòng, loại phòng, giá phòng  
- Quản lý doanh thu, thống kê đặt phòng  
- Quản lý tài khoản nhân viên và báo cáo tổng hợp  

---

## 🗄️ Database
Cơ sở dữ liệu chính bao gồm các bảng:
- `users` (người dùng)
- `rooms` (phòng)
- `room_types` (loại phòng)
- `bookings` (đặt phòng)
- `payments` (thanh toán)
- `reviews` (đánh giá)
- `staff` (nhân viên)
- `reports` (báo cáo)

---

## 🧩 Công nghệ sử dụng
- **Backend:** Python (Flask / Django) + MySQL  
- **Frontend:** HTML / CSS / JavaScript  
- **Database:** MySQL  
- **Testing:** Pytest (unit test), Selenium (integration test)  
- **Quản lý mã nguồn:** Git + GitHub  
- **Mô hình phát triển:** Agile – Scrum  

---

## 🖼️ Sơ đồ Use Case
![Use Case Diagram](https://github.com/n23dcpt094-phanngocthienminh/btapcnpm/blob/main/lab/lab02_usecase/use_case.png?raw=true)

---

## ⚙️ Cài đặt & chạy thử
Clone repo về máy:
```bash
git clone https://github.com/n23dcpt094-phanngocthienminh/btapcnpm.git
cd btapcnpm
