# Week 6 - FashionMNIST voi PyTorch

## Gioi thieu
Lab nay huong dan xay dung mot mo hinh mang no-ron don gian de phan loai anh thoi trang trong bo du lieu FashionMNIST bang PyTorch.

Noi dung chinh trong notebook `lab6.ipynb`:
- Nap du lieu FashionMNIST.
- Tao `Dataset` tuy chinh (`FMNISTDataset`).
- Tao `DataLoader` voi batch size = 32.
- Dinh nghia mo hinh `nn.Sequential`.
- Huan luyen mo hinh va do luong do chinh xac.
- Ve do thi Loss va Accuracy theo epoch.

## Cau truc thu muc
- `lab6.ipynb`: Notebook chinh cua buoi hoc.
- `archive/`: Thu muc chua du lieu dau vao can thiet cho bai toan.

## Yeu cau moi truong
Can cai dat cac goi Python sau:
- `torch`
- `torchvision`
- `numpy`
- `matplotlib`

Vi du cai dat nhanh:
```bash
pip install torch torchvision numpy matplotlib
```

## Cach chay
1. Mo file `lab6.ipynb`.
2. Chay lan luot tung cell tu tren xuong duoi.
3. Quan sat:
- Gia tri loss giam dan qua cac epoch.
- Do chinh xac tang dan qua cac epoch.
- Bieu do Loss/Accuracy o cuoi notebook.

## Ghi chu quan trong
- Notebook tu dong su dung GPU neu co (`cuda`), neu khong se chay tren CPU.
- Du lieu duoc tai ve qua `torchvision.datasets.FashionMNIST(..., download=True)` khi can.
- Ban co the thu nghiem them phien ban chuan hoa dau vao (`x / 255`) de so sanh hieu qua.

## Loi thuong gap
- Loi khong tim thay du lieu: kiem tra duong dan va quyen ghi thu muc `archive/`.
- Loi thieu thu vien: cai dat lai cac goi trong phan "Yeu cau moi truong".
- Chay cham tren CPU: giam so epoch hoac giam kich thuoc mo hinh.

## Muc tieu dau ra
Sau khi hoan thanh lab, ban co the:
- Hieu quy trinh huan luyen mo hinh phan loai anh voi PyTorch.
- Viet `Dataset`/`DataLoader` co ban.
- Theo doi va danh gia hieu nang bang Loss va Accuracy.
