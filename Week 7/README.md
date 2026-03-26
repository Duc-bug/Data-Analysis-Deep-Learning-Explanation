# Week 7 - CNN Training với GPU

## Giới thiệu
Lab này hướng dẫn xây dựng và huấn luyện một mô hình Convolutional Neural Network (CNN) với hỗ trợ GPU bằng PyTorch. Mô hình được thiết kế để phân loại ảnh đầu vào kích thước $128 \times 128$ pixel với 6 lớp: BIODEGRADABLE, CARDBOARD, GLASS, METAL, PAPER, PLASTIC.

Nội dung chính trong notebook `cnn_gpu_train.ipynb`:
- Kiểm tra khả năng GPU và thiết bị huấn luyện.
- Định nghĩa kiến trúc CNN với 3 khối tích chập (Conv block).
- Chuẩn bị dữ liệu từ định dạng YOLO.
- Xây dựng vòng lặp huấn luyện (training loop).
- Huấn luyện mô hình với giám sát (validation).
- Đánh giá performance trên tập test.
- Vẽ biểu đồ Loss và Accuracy.

## Cấu trúc thư mục
```
Week 7/
├── README.md              # File này
├── cnn_gpu_train.ipynb    # Notebook chính
└── archive/               # Thư mục chứa dữ liệu huấn luyện
    ├── training_set/      # Dữ liệu huấn luyện
    ├── test_set/          # Dữ liệu kiểm tra
    └── FashionMNIST/      # Dữ liệu FashionMNIST (nếu có)
```

## Yêu cầu môi trường
Cần cài đặt các gói Python sau:
- `torch` (PyTorch) - Framework deep learning
- `torchvision` - Các công cụ xử lý hình ảnh cho PyTorch
- `numpy` - Thư viện tính toán số
- `matplotlib` - Vẽ biểu đồ
- `pillow` - Xử lý ảnh (PIL)

### Cài đặt nhanh
```bash
pip install torch torchvision numpy matplotlib pillow
```

### Cài đặt với GPU (CUDA)
Nếu bạn có GPU NVIDIA, cài đặt phiên bản PyTorch hỗ trợ CUDA:
```bash
# Xem chi tiết tại: https://pytorch.org
# Ví dụ với CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Cách chạy

### Bước 1: Chuẩn bị dữ liệu
Đảm bảo dữ liệu huấn luyện có cấu trúc YOLO trong thư mục `archive/`:
- Dữ liệu hình ảnh và nhãn (labels)
- Định dạng nhãn: `class_id center_x center_y width height` (tọa độ chuẩn hóa)

### Bước 2: Chạy notebook
1. Mở file `cnn_gpu_train.ipynb`.
2. Chạy lần lượt từng cell từ trên xuống dưới.
3. Notebook sẽ tự động:
   - Kiểm tra GPU availability
   - Tạo cropped images từ dữ liệu YOLO
   - Huấn luyện mô hình
   - Validation sau mỗi epoch
   - Vẽ biểu đồ kết quả

## Chi tiết các khối trong Notebook

### 1. Cài đặt thiết bị và Định nghĩa mô hình
Định nghĩa kiến trúc CNN với:
- **Conv Block 1**: 3 channels → 32 filters (3×3 kernel)
- **Conv Block 2**: 32 filters → 64 filters (3×3 kernel)
- **Conv Block 3**: 64 filters → 128 filters (3×3 kernel)
- **Fully Connected**: 2 lớp fully connected (FC) với dropout 0.5
- **Output**: 6 lớp (phân loại rác)

Mô hình sẽ tự động chạy trên GPU (nếu có) hoặc CPU.

### 2. Vòng lặp Huấn luyện
Quá trình huấn luyện bao gồm:
- **Training Phase**: Tính loss, backward pass, update weights
- **Validation Phase**: Đánh giá trên validation set
- **Metrics**: Loss, Accuracy theo epoch
- **Early Stopping** (tùy chọn): Dừng sớm nếu performance không cải thiện

### 3. Xử lý dữ liệu YOLO
Notebook tự động:
- Đọc nhãn YOLO (tọa độ bounding box chuẩn hóa)
- Cắt cropped images từ dữ liệu gốc
- Tổ chức theo 6 lớp
- Tạo DataLoader cho training/validation/test

## Ghi chú quan trọng

### GPU vs CPU
- **Với GPU**: Huấn luyện nhanh hơn 5-10 lần
- **Notebook tự chọn**: Sử dụng GPU nếu có (`torch.cuda.is_available()`), ngược lại dùng CPU
- **Kiểm tra**: Cell đầu tiên sẽ in ra thiết bị đang sử dụng

### Hyperparameters
- **Learning rate**: 0.001 (Adam optimizer)
- **Batch size**: 32 (có thể điều chỉnh)
- **Số epochs**: Tuỳ dữ liệu (hãy quan sát validation loss)
- **Dropout**: 0.5 (ngăn overfitting)

### Kích thước input
- Hình ảnh được resize về **128×128 pixels**
- **3 channels** (RGB)
- Output sau pooling 3 lần: 16×16 features

## Lỗi thường gặp

| Lỗi | Nguyên nhân | Giải pháp |
|-----|------------|----------|
| `CUDA out of memory` | Batch size quá lớn | Giảm batch size hoặc dùng CPU |
| `No such file or directory` | Dữ liệu không tồn tại | Kiểm tra đường dẫn `DATA_ROOT` |
| `AssertionError in _parse_yolo_row` | Format YOLO sai | Kiểm tra file nhãn (5 giá trị per dòng) |
| `RuntimeError: Expected 3D input` | Hình ảnh grayscale | Chuyển sang RGB trước khi đưa vào model |
| Huấn luyện rất chậm | GPU không được dùng | Cài CUDA version đúng hoặc dùng CPU |

## Kết quả mong đợi

Sau khi hoàn thành lab, bạn sẽ có:
- ✅ Mô hình CNN đã huấn luyện có thể phân loại rác
- ✅ Biểu đồ Loss/Accuracy qua epochs
- ✅ Model weights lưu trữ (nếu code có save model)
- ✅ Hiểu biết về image classification với deep learning
- ✅ Kỹ năng sử dụng PyTorch và GPU training

### Benchmark Performance
- **Accuracy trên validation set**: Mong đợi 80-95% (tuỳ dữ liệu)
- **Training time**: 
  - Với GPU (RTX series): 5-15 phút / 50 epochs
  - Với CPU: 30-60 phút / 50 epochs

## Mở rộng (Bonus)

1. **Thử các kiến trúc khác**:
   - ResNet, VGG, MobileNet (với pretrained weights)

2. **Cải thiện dữ liệu**:
   - Data augmentation (rotation, flip, brightness)
   - Oversampling/undersampling các lớp imbalanced

3. **Optimize mô hình**:
   - Learning rate scheduling
   - Batch normalization
   - Weight decay (L2 regularization)

4. **Deploy mô hình**:
   - Lưu model để dùng sau: `torch.save(model.state_dict(), 'model.pth')`
   - Tạo inference script

## Tài liệu tham khảo
- **PyTorch Documentation**: https://pytorch.org/docs/
- **CNN Fundamentals**: https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
- **Image Classification**: https://pytorch.org/vision/main/models.html

## Liên hệ / Hỗ trợ
Nếu gặp vấn đề, hãy:
1. Kiểm tra báo lỗi (error message)
2. Xem phần "Lỗi thường gặp" trên
3. Các cell output để debug
