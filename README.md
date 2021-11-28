# Overview Jurnal
Dataset yang digunakan dalam jurnal adalah <i>American Sign Language</i> bersumber dari Kaggle. Jurnal tersebut melakukan perbandingan algoritma klasifikasi citra antara Convolutional Neural Network (CNN) dan Multilayer Perceptron (MLP) untuk mengenali bahasa isyarat alfabet American Sign Language. Metode preprocessing yang digunakan adalah Gaussian Low Pass Filtering dan Laplacian High Pass Filtering karena dapat menghilangkan noise dan mempertajam citra. Pada jurnal tersebut MLP dan CNN dibagi menjadi 3 versi yaitu tanpa preprocessing, dengan Gaussian Low Pass Filtering, dan dengan Laplacian Filtering. Hal ini dilakukan untuk mengetahui pengaruh jenis preprocessing terhadap performa yang dihasilkan. 2 versi model yang digunakan dalam CNN adalah :
1. CNN-1 dengan 3 proses convolution, 2 proses pooling, 3 fully connected layer

- Summary1 layer model CNN-1 ditunjukkan pada gambar berikut :

![ha2](https://user-images.githubusercontent.com/62975150/143726115-90340add-1707-4fff-82ed-5daa645604a2.jpg)

2. CNN-2 dengan 4 proses convolution, 2 proses pooling, 3 fully connected layer

- Summary2 layer model CNN-2 ditunjukkan pada gambar berikut :

![aaa](https://user-images.githubusercontent.com/62975150/143726046-e43a2161-65a1-4436-844f-53a2d7377049.jpg)

Parameter yang dibutuhkan adalah activation function, kernel size, tipe pooling, dan dropout. Sedangkan dense pada hidden layer menggunakan activation function ReLu dan Dense output layer menggunakan softmax. Dari algoritma CNN tersebut menghasilkan akurasi sebesar 96,97% dan F1 score 96,93%. sedangkan MLP mendapatkan akurasi terbaik 74,79% tanpa melalui preprocessing.

# Overview Dataset
Dataset yang digunakan  adalah <a href="https://www.kaggle.com/grassknoted/asl-alphabet"><i>American Sign Language</i></a> yang didapatkan dari open source kaggle.com. Dalam dataset tersebut, Kumpulan data training berisi 87.000 gambar berukuran 200x200 pixel. Ada 29 kelas, 26 di antaranya untuk huruf A-Z dan 3 kelas untuk SPACE, DELETE dan NOTHING.
3 kelas ini sangat membantu dalam aplikasi real-time, dan klasifikasi. Kumpulan data testing hanya berisi 29 gambar, untuk mendorong penggunaan gambar testing di dunia nyata.
Persentase perbandingan data training adalah 90% dan 10% data testing. Contoh dataset ditunjukkan pada gambar berikut :

<img width="482" alt="ASL Lang" src="https://user-images.githubusercontent.com/64589800/138824570-78c10825-e839-4c89-bb6c-8329a22fea50.png">

## Preprocessing
<a href="https://github.com/AaliyahLusianti074/TugasPraktikumML_066-074/blob/main/PreprocessingData.py">Preprocessing</a> pada dataset dilakukan dengan membagi data training dan data testing dengan perbandingan 9:1. Kelas dataset memiliki 29 gambar terdiri dari gambar ASL huruf A sampai dengan Z serta 'nothing', 'space' dan 'del'. Pembagian dataset terbagi sebanyak 78300 gambar data training dan sisanya 8700 sebagai data testing dengan size(32,32).

## Modelling
Model Convolutional Neural Network (CNN) yang digunakan pada dataset terbagi menjadi 2, yakni model VGG16 dan MaxPooling2D. 
- Summary1 layer model CNN-1 VGG16 ditunjukkan pada gambar berikut :

![plot222](https://user-images.githubusercontent.com/62975150/143670802-01643110-8d13-4a5b-a03a-8b983f0b06fd.jpg)

- Matriks evaluation1 yang dihasilkan :

![matriks1_1](https://user-images.githubusercontent.com/62975150/143729281-5eae83eb-575b-4779-865b-8ba46f721929.jpg)

- Graph akurasi1 dan loss

![graphm1_1](https://user-images.githubusercontent.com/62975150/143727380-09073453-1297-40c1-9f00-3aecaba11ba4.jpg)

- Summary2 layer model CNN-2 MaxPooling2D ditunjukkan pada gambar berikut :

![ada](https://user-images.githubusercontent.com/62975150/143671447-fb40f149-7d06-4992-987e-d630b0ff5e19.jpg)

- Matriks evaluation2 yang dihasilkan :
- Graph akurasi2 dan loss2

![graphm2_2](https://user-images.githubusercontent.com/62975150/143727335-97d7e2b9-9659-4fcb-afee-698218d7139e.jpg)

## Predict
Hasil prediksi gambar dataset pada sample gambar:
-Hasil prediksi pada model 1 yang dilakukan pada gambar A_test.jpg menunjukkan hasil prediksi index [0] yang berarti menunujukkan huruf A, dilihat pada output berukut:

![pred_1_1](https://user-images.githubusercontent.com/62975150/143729424-3c51748a-4a25-4942-811d-cbb6b1716b2a.jpg)









