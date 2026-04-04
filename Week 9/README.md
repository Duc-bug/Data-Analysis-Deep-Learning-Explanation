# Week 9 - FashionMNIST + Deploy Flask

## Gioi thieu
Week 9 huan luyen mo hinh phan loai FashionMNIST va luu trong so vao file `.pth`.
Ban co the dung ngay file da luu de suy luan tren web Flask.

## Tep quan trong
- `Trainweek9.ipynb`: Notebook huan luyen.
- `checkpoints/fmnist_mlp_weights.pth`: Trong so model.
- `checkpoints/fmnist_mlp_checkpoint.pth`: Checkpoint day du (model + optimizer + lich su).
- `flask_app/app.py`: Web Flask du doan anh upload.

## Chay notebook
1. Mo `Trainweek9.ipynb`.
2. Chay lan luot cac cell.
3. Chay cell luu model de tao/ghi de file `.pth` trong `checkpoints/`.

## Chay web Flask de du doan anh
### 1) Cai thu vien
Di chuyen vao thu muc app va cai dependencies:

```bash
cd "Week 9/flask_app"
pip install -r requirements.txt
```

### 2) Chay server
```bash
python app.py
```

### 3) Mo trinh duyet
Vao dia chi:
- `http://127.0.0.1:5000`

Tai anh len, he thong se tra ve:
- Nhan du doan top-1
- Top-3 xac suat

## Luu y ve nhan du doan
Model Week 9 duoc huan luyen tren FashionMNIST, nen cac nhan tra ve la:
- T-shirt_top
- Trouser
- Pullover
- Dress
- Coat
- Sandal
- Shirt
- Sneaker
- Bag
- Ankle_boot

Neu ban muon du doan "dog/cat" thi can model duoc train tren du lieu dog/cat va thay file `.pth` + class mapping tuong ung.
