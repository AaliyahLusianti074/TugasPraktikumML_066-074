# Overview Jurnal
Dataset yang digunakan dalam <a href="http://www.scielo.org.mx/pdf/cys/v24n3/1405-5546-cys-24-03-1211.pdf">Jurnal Referensi</a> adalah <a href="https://www.kaggle.com/grassknoted/asl-alphabet"><i>American Sign Language</i></a> bersumber dari Kaggle. dataset terdiri dari 26 tanda alfabet ASL (dari
A sampai Z) dan 3 kelas berlabel “SPACE”, “DEL” dan “NOTHING”. Jurnal berjudul <b>Siamese Convolutional Neural Network for ASL Alphabet Recognition</b> tersebut menggunakan dua model Convolutional Neural Network yang terdiri dari 8 convolutional dan 3 fully connected (Dense) layer. Training dilakukan dengan menggunakan Keras Tensorflow sebagai framework di Google Colab platform dengan GPU. Setelah 30 epoch, train_loss dan train_accuracy masing-masing 0.0164 dan 0.9870, dan mencapai val_loss dan val_accuracy 0,0245 dan 0,9764.

Summary layer model CNN ditunjukkan pada gambar berikut :

<img width="300" alt="yyy" src="https://user-images.githubusercontent.com/64589800/147534215-b050b2c8-0147-4272-b2d5-79481be8ae26.png">

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

![matriks2_2](https://user-images.githubusercontent.com/62975150/143729819-f5d17ac8-babe-4891-ad9b-3fafb77a7d70.jpg)

- Graph akurasi2 dan loss2

![graphm2_2](https://user-images.githubusercontent.com/62975150/143727335-97d7e2b9-9659-4fcb-afee-698218d7139e.jpg)

## Predict
Hasil prediksi gambar dataset pada sample gambar:
- Hasil prediksi pada model 1 yang dilakukan pada gambar A_test.jpg menunjukkan hasil prediksi index [0] yang berarti menunujukkan huruf A, dilihat pada output berukut:

![pred_1_1](https://user-images.githubusercontent.com/62975150/143729424-3c51748a-4a25-4942-811d-cbb6b1716b2a.jpg)

- Hasil prediksi pada model 2 yang dilakukan pada gambar C_test.jpg menunjukkan hasil prediksi index [2] yang berarti menunujukkan huruf C, dilihat pada output berukut:

![pred2_2](https://user-images.githubusercontent.com/62975150/143729687-3b9fc0e2-ec01-4c4b-bb3f-d524795ea820.jpg)








