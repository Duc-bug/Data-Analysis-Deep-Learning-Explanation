# Week 8 - NLP voi NLTK

## Gioi thieu
Tuan 8 tap trung vao xu ly ngon ngu tu nhien (Natural Language Processing - NLP) voi thu vien NLTK.
Noi dung di tu thao tac co ban voi corpus, phan tich tu vung, n-gram, xu ly van ban tu web/HTML den bai toan phan loai cam xuc.

## Noi dung chinh
1. Lam quen voi NLTK va corpus Gutenberg.
2. Tim kiem tu trong van ban voi concordance, common contexts, similar words.
3. Phan tich tan so tu:
- FreqDist cho toan bo van ban.
- Loai stopwords.
- Loai them dau cau de lay tu khoa quan trong.
4. Lam viec voi n-gram:
- Bigram
- Trigram
5. Loc tu theo dieu kien:
- Tu dai hon mot nguong ky tu.
- Tu chua chuoi con (vi du: ious).
6. Doc van ban tu internet bang urllib.
7. Rut trich noi dung van ban tu HTML voi BeautifulSoup.
8. Phan tich cam xuc co ban voi movie_reviews va Naive Bayes.
9. Bai tap mo rong:
- Liet ke corpus.
- Stopwords da ngon ngu.
- WordNet (dong nghia, trai nghia).
- Tagset POS.
- So sanh do tuong dong giua hai danh tu bang WordNet.

## Tep su dung
- file.ipynb: Notebook chinh cua tuan 8.

## Yeu cau moi truong
Can cai cac thu vien:
- nltk
- beautifulsoup4
- lxml

Lenh cai dat:
```bash
pip install nltk beautifulsoup4 lxml
```

## Tai nguyen NLTK can tai
Trong notebook, co the can tai them du lieu:
- stopwords
- punkt
- movie_reviews
- wordnet
- omw-1.4
- tagsets

Vi du:
```python
import nltk
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("movie_reviews")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("tagsets")
```

## Cach chay
1. Mo notebook cua tuan 8.
2. Chay tung cell tu tren xuong duoi.
3. Neu gap loi thieu resource, tai them bang nltk.download nhu phan tren.
4. Voi phan lay du lieu web, can co ket noi mang on dinh.

## Ket qua mong doi
Sau khi hoan thanh tuan 8, ban co the:
- Su dung corpus trong NLTK de kham pha du lieu van ban.
- Thuc hien tien xu ly van ban co ban.
- Phan tich tan so tu va n-gram.
- Rut trich text tu web va HTML.
- Xay dung mo hinh phan loai cam xuc don gian voi Naive Bayes.
- Su dung WordNet de tra nghia, tu dong nghia/trai nghia va do tuong dong tu.

## Loi thuong gap va cach xu ly
1. LookupError: Resource ... not found
- Nguyen nhan: chua tai du lieu NLTK.
- Cach xu ly: chay nltk.download voi resource tuong ung.

2. UnicodeDecodeError hoac loi encoding
- Nguyen nhan: dung sai encoding khi decode.
- Cach xu ly: uu tien utf8 hoac utf-8-sig tuy nguon du lieu.

3. Loi khi doc trang web
- Nguyen nhan: trang chan request mac dinh.
- Cach xu ly: them User-Agent khi gui request.

4. IndexError khi truy cap synsets
- Nguyen nhan: dung chuoi synset sai dinh dang voi synsets.
- Cach xu ly:
	- Dung wordnet.synset voi id day du, vi du dog.n.01.
	- Hoac dung wordnet.synsets("dog", pos=wordnet.NOUN).

## Goi y mo rong
- Thu them stemming/lemmatization.
- So sanh mo hinh Naive Bayes voi Logistic Regression hoac SVM.
- Them buoc lam sach du lieu ky hon truoc khi huan luyen.

