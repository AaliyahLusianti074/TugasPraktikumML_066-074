# Overview Jurnal
Dataset yang digunakan dalam jurnal adalah <i>American Sign Language</i> bersumber dari Kaggle. Jurnal tersebut melakukan perbandingan allgoritma klasifikasi citra antara Convolutional Neural Network (CNN) dan Multilayer Perceptron (MLP) untuk mengenali bahasa isyarat alfabet American Sign Language. Metode preprocessing yang digunakan adalah Gaussian Low Pass Filtering dan Laplacian High Pass Filtering karena dapat menghilangkan noise dan mempertajam citra. Pada jurnal tersebut MLP dan CNN dibagi menjadi 3 versi yaitu tanpa preprocessing, dengan Gaussian Low Pass Filtering, dan dengan Laplacian Filtering. Hal ini dilakukan untuk mengetahui pengaruh jenis preprocessing terhadap performa yang dihasilkan. 2 versi model yang digunakan dalam CNN adalah :
1. CNN-1 dengan 3 proses convolution, 2 proses pooling, 3 fully connected layer
2. CNN-2 dengan 4 proses convolution, 2 proses pooling, 3 fully connected layer
Parameter yang dibutuhkan adalah activation function, kernel size, tipe pooling, dan dropout. Sedangkan dense pada hidden layer menggunakan activation function ReLu dan Dense output layer menggunakan softmax.
Dari algoritma CNN tersebut menghasilkan akurasi sebesar 96,97% dan F1 score 96,93%. sedangkan MLP mendapatkan akurasi terbaik 74,79% tanpa melalui preprocessing.

## Dataset
Dataset yang digunakan  adalah <a href="https://www.kaggle.com/grassknoted/asl-alphabet">ASL Language</a> yang didapatkan dari open source kaggle.com.
Dalam dataset tersebut, Kumpulan data training berisi 87.000 gambar berukuran 200x200 pixel.
Ada 29 kelas, 26 di antaranya untuk huruf A-Z dan 3 kelas untuk SPACE, DELETE dan NOTHING.
3 kelas ini sangat membantu dalam aplikasi real-time, dan klasifikasi.
Kumpulan data testing hanya berisi 29 gambar, untuk mendorong penggunaan gambar testing di dunia nyata.

<img width="482" alt="ASL Lang" src="https://user-images.githubusercontent.com/64589800/138824570-78c10825-e839-4c89-bb6c-8329a22fea50.png">

## Preprocessing

Preprocessing pada dataset <a href="https://github.com/AaliyahLusianti074/TugasPraktikumML_066-074/blob/main/PreprocessingData.py">Preprocessing.py</a> dilakukan dengan membagi data training dan data testing dengan perbandingan 9:1.
Kelas dataset memiliki 29 gambar terdiri dari gambar ASL huruf A sampai dengan Z serta 'nothing', 'space' dan 'del'.
Pembagian dataset terbagi sebanyak 78300 gambar data training dan sisanya 8700 sebagai data testing dengan shape 32x32.

## Modelling

Build model dataset menjadi 2, yakni model VGG16 dan MaxPooling2D.
Ditemukan akurasi sebesar 99% pada model VGG16 dan 75% pada model MaxPooling2D.

SUMMARY LAYER MODEL 1 - VGG 16

![plot222](https://user-images.githubusercontent.com/62975150/143670802-01643110-8d13-4a5b-a03a-8b983f0b06fd.jpg)

SUMMARY LAYER MODEL 2 - MAXPOOLING

![ada](https://user-images.githubusercontent.com/62975150/143671447-fb40f149-7d06-4992-987e-d630b0ff5e19.jpg)

# Evaluasi
