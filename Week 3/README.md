# Lab3 - Data Cleaning (Làm sạch dữ liệu)
## Mô tả
Lab thực hành về các kỹ thuật làm sạch dữ liệu cơ bản trên tập dữ liệu nhịp tim bệnh nhân.
## Công nghệ sử dụng
- **pandas**: Xử lý và phân tích dữ liệu
## Cấu trúc file
- `lab3.ipynb`: Notebook chứa code thực hành
- `patient_heart_rate.csv`: Dữ liệu gốc (chưa làm sạch)
- `patient_heart_rate_clean.csv`: Dữ liệu đã được làm sạch
- `outputcleaning.csv`: File trung gian sau bước 10

## Các vấn đề xử lý

1. **Missing header**: Thêm tên cột cho CSV
2. **Multiple data in one column**: Tách cột Name thành Firstname và Lastname
3. **Unit inconsistency**: Chuẩn hóa đơn vị Weight về kg
4. **Empty rows**: Xóa các dòng rỗng
5. **Duplicate records**: Loại bỏ dữ liệu trùng lặp
6. **Non-ASCII characters**: Xử lý ký tự đặc biệt
7. **Missing values**: Điền giá trị thiếu cho Age bằng mean
8. **Column splitting**: Phân tách cột chứa nhiều thông tin (giới tính + thời gian)
9. **Advanced missing value handling**: Xử lý pulse_rate thiếu theo nhiều mức độ ưu tiên
10. **Data optimization**: Rút gọn và reindex dữ liệu

