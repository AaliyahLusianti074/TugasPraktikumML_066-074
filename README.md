# Overview
Anggota Kelompok :           
- ELA EFRIYANTI     (201810370311066)
- AALIYAH LUSIANTI  (201810370311074)

# Dataset
Dataset yang digunakan  adalah <a href="https://www.kaggle.com/grassknoted/asl-alphabet">ASL Language</a> yang didapatkan dari open source kaggle.com.
Dalam dataset tersebut, Kumpulan data training berisi 87.000 gambar berukuran 200x200 pixel.
Ada 29 kelas, 26 di antaranya untuk huruf A-Z dan 3 kelas untuk SPACE, DELETE dan NOTHING.
3 kelas ini sangat membantu dalam aplikasi real-time, dan klasifikasi.
Kumpulan data testing hanya berisi 29 gambar, untuk mendorong penggunaan gambar testing di dunia nyata.

<img width="482" alt="ASL Lang" src="https://user-images.githubusercontent.com/64589800/138824570-78c10825-e839-4c89-bb6c-8329a22fea50.png">

# Preprocessing

Preprocessing pada dataset ( PreprocessingData.py ) dilakukan dengan membagi data training dan data testing dengan perbandingan 9:1.
Kelas dataset memiliki 29 gambar terdiri dari gambar ASL huruf A sampai dengan Z serta 'nothing', 'space' dan 'del'.
Pembagian dataset terbagi sebanyak 78300 gambar data training dan sisanya 8700 sebagai data testing dengan shape 32x32.

# Modelling

Build model dataset menjadi 2, yakni model VGG16 dan MaxPooling2D.
Ditemukan akurasi sebesar 99% pada model VGG16 dan 75% pada model MaxPooling2D.

SUMMARY LAYER MODEL 1 - VGG 16
![plot222](https://user-images.githubusercontent.com/62975150/143670691-c93acde2-49c2-43f1-affa-d97650259194.jpg)


# Evaluasi
