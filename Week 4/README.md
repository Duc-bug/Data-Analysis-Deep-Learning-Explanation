# Week 4: Phân tích dữ liệu Titanic

## Mô tả
Lab 4 thực hành phân tích dữ liệu thảm họa tàu Titanic, bao gồm làm sạch dữ liệu, xây dựng đặc trưng và khám phá dữ liệu.

## Nội dung chính

### Phần 1: Data Cleansing & Feature Engineering
- Tải và khám phá dữ liệu Titanic
- Xử lý dữ liệu thiếu (Age, Cabin, Embarked)
- Tách và xử lý cột Name thành Firstname, Lastname
- Rút gọn giá trị cột Sex (M/F)
- Tạo nhóm tuổi (Agegroup): Kid, Teen, Adult, Older
- Trích xuất danh xưng (namePrefix): Mr, Mrs, Miss, Master
- Tính kích thước gia đình (familySize) và trạng thái đi một mình (Alone)
- Phân loại cabin (typeCabin)

### Phần 2: Exploratory Data Analysis (EDA)
- Phân tích tỉ lệ sống sót theo giới tính
- Phân tích tỉ lệ sống sót theo hạng vé (Pclass)
- Phân tích tỉ lệ sống sót theo nhóm tuổi và giới tính
- Phân tích xác suất sống sót theo kích thước nhóm đi cùng
- Phân tích mối quan hệ giữa giá vé và tỉ lệ sống sót
- Phân tích sống sót theo hạng vé và cảng xuất phát (Embarked)

## Dataset
- `titanic_disaster.csv`: Dữ liệu hành khách tàu Titanic

## Thư viện sử dụng
- pandas, numpy
- matplotlib, seaborn