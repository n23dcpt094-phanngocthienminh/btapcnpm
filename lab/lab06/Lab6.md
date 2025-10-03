# Lab 06 – Thiết kế chi tiết lớp & kiến trúc ATM

## Mục tiêu
- Từ Use Case và Sequence Diagram, xây dựng **Class Diagram** và **Package Diagram** cho hệ thống ATM.  
- Áp dụng PlantUML/draw.io để mô hình hóa và xuất file ảnh PNG.  

## Nội dung thực hiện

### 1. Class Diagram
- Các lớp chính:  
  - **ATM**: quản lý giao dịch, xác thực, rút tiền, gửi tiền, chuyển khoản.  
  - **Card**: thông tin thẻ (số thẻ, mã PIN, trạng thái).  
  - **Account**: tài khoản, số dư, phương thức debit/credit.  
  - **Transaction**: lưu chi tiết giao dịch (mã, loại, số tiền, thời gian, trạng thái).  

👉 Quan hệ:  
- ATM liên kết với Card và Transaction.  
- Card liên kết với Account.  
- Account liên kết với Transaction.  

### 2. Package Diagram
- **UI**: giao diện với người dùng (ATMUI).  
- **Controller**: xử lý luồng logic chính (ATMController).  
- **BankService**: kết nối tới ngân hàng (BankServer).  
- **Hardware**: phần cứng ATM (CardReader, CashDispenser, DepositSlot).  

👉 Quan hệ:  
- UI gọi Controller.  
- Controller điều phối giữa BankService và Hardware.  
- Hardware tương tác với BankService để xác thực & thực hiện giao dịch.  

### 3. Kết quả
- Xuất được **2 sơ đồ PNG**:  
  - `class-atm.png` (Class Diagram)  
  - `package-atm.png` (Package Diagram)  
- Mô hình giúp tách biệt rõ trách nhiệm giữa các thành phần, dễ dàng bảo trì và mở rộng hệ thống ATM.  

## Ghi chú
- Class Diagram mô tả các thực thể chính: **ATM, Card, Account, Transaction**.  
- Package Diagram thể hiện kiến trúc **4 lớp**: UI, Controller, BankService, Hardware.  
- Đây là mô hình chuẩn hóa giúp **tách biệt trách nhiệm**, **giảm phụ thuộc**, và **tăng khả năng mở rộng** của hệ thống ATM.  
