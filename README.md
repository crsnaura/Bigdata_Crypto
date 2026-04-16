# Pengembangan Intelligent Cryptocurrency Market Intelligence System

## Berbasis Data Pipeline dan Machine Learning

---

## Nama Anggota Kelompok

* Gaitsa Nazwa Kansa (24083010014)
* Auliya Khotimatuz Zahroh (24083010061)
* Carissa Naura Rajwa (24083010063)

---

## Latar Belakang dan Konsep Project

Perkembangan pasar cryptocurrency dalam beberapa tahun terakhir menunjukkan dinamika harga yang sangat fluktuatif. Perubahan harga yang cepat sering kali menyulitkan investor dalam menentukan keputusan investasi yang tepat. Berdasarkan permasalahan tersebut, proyek ini mengembangkan sebuah sistem analisis pasar cryptocurrency yang mampu mengolah data secara otomatis dan menyajikan informasi yang informatif serta mudah dipahami. Sistem ini dirancang untuk mengintegrasikan proses pengambilan data, pengolahan data, analisis, hingga visualisasi dalam satu alur yang terstruktur. Dengan adanya sistem ini, diharapkan pengguna dapat memperoleh gambaran kondisi pasar secara lebih komprehensif sehingga dapat mendukung proses pengambilan keputusan.

---

## Sumber Data

Data yang digunakan dalam proyek ini diperoleh dari API publik milik CoinGecko, yang menyediakan informasi pasar cryptocurrency secara real-time.

Aset cryptocurrency yang digunakan dalam penelitian ini meliputi:

* Bitcoin (BTC)
* Ethereum (ETH)
* Solana (SOL)
* Dogecoin (DOGE)
* Binance Coin (BNB)

Variabel utama yang digunakan dalam dataset antara lain:

* timestamp atau date
* price (harga aset)
* market_cap (kapitalisasi pasar)
* volume (volume perdagangan)

Data historis dikumpulkan selama kurang lebih 90 hari dengan frekuensi tinggi (hourly), kemudian disimpan dalam format CSV untuk memudahkan proses analisis.

---

## Sistem yang Dibangun

Sistem yang dikembangkan terdiri dari beberapa komponen utama sebagai berikut:

### 1. Data Collection

Data cryptocurrency diambil secara otomatis dari API CoinGecko menggunakan bahasa pemrograman Python.

### 2. Data Pipeline

Data yang diperoleh diproses melalui beberapa tahapan, yaitu:

* pembersihan data (data cleaning)
* penanganan missing values
* penyelarasan waktu (resampling)
* transformasi data

Tahapan ini bertujuan untuk menghasilkan dataset yang konsisten dan siap digunakan untuk analisis.

---

### 3. Feature Engineering

Pada tahap ini dilakukan pembentukan variabel baru untuk mendukung analisis, antara lain:

* cumulative return (untuk melihat performa aset)
* log return (untuk analisis perubahan harga)
* volatility (untuk mengukur tingkat risiko)
* indikator tren pasar (bullish atau bearish)

---

### 4. Analisis Data dan Visualisasi

Hasil pengolahan data disajikan dalam bentuk dashboard interaktif berbasis Streamlit. Fitur utama yang disediakan antara lain:

* Key metrics (harga terkini, return, volatilitas, dan kondisi pasar)
* Grafik pergerakan harga (time series)
* Analisis korelasi antar cryptocurrency
* Analisis tren pasar
* Simulasi portofolio investasi
* Integrasi harga real-time

Dashboard ini dirancang untuk memudahkan pengguna dalam memahami data secara visual.

---

### 5. Machine Learning (Pengembangan Lanjutan)

Sebagai pengembangan lanjutan, sistem ini dirancang untuk mengimplementasikan model machine learning dengan tujuan:

* memprediksi harga cryptocurrency pada periode mendatang
* mengklasifikasikan kondisi pasar (bullish, bearish, atau sideways)

Model akan memanfaatkan fitur-fitur yang telah dibentuk pada tahap feature engineering.

---

## Tujuan Pengembangan Sistem

Tujuan utama dari proyek ini adalah:

* membangun pipeline pengolahan data cryptocurrency berbasis API
* menganalisis pola pergerakan harga cryptocurrency
* mengembangkan model machine learning untuk prediksi dan klasifikasi pasar
* menyajikan hasil analisis dalam bentuk dashboard interaktif

---

## Karakteristik Big Data (7V)

### 1. Volume

Dataset yang digunakan terdiri dari ribuan baris data historis untuk beberapa jenis cryptocurrency, sehingga mencerminkan skala data yang cukup besar.

### 2. Velocity

Data diperoleh dari API dengan frekuensi tinggi serta dapat diperbarui secara berkala, menunjukkan kecepatan aliran data yang tinggi.

### 3. Variety

Data memiliki beragam atribut seperti harga, kapitalisasi pasar, dan volume transaksi, serta mencakup beberapa jenis cryptocurrency.

### 4. Veracity

Data telah melalui proses pembersihan dan validasi sehingga kualitas dan keandalannya dapat dijaga.

### 5. Value

Sistem menghasilkan informasi yang bernilai, seperti tren pasar, tingkat volatilitas, dan korelasi antar aset yang dapat digunakan dalam pengambilan keputusan.

### 6. Variability

Pergerakan harga cryptocurrency yang fluktuatif menunjukkan adanya variasi data yang tinggi dari waktu ke waktu.

### 7. Visualization

Data disajikan dalam bentuk visualisasi interaktif sehingga memudahkan pengguna dalam memahami pola dan insight yang dihasilkan.

---

## Teknologi yang Digunakan

* Python
* Streamlit
* Pandas
* Matplotlib dan Seaborn
* API CoinGecko

---

## Cara Menjalankan Sistem

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Kesimpulan

Proyek ini menunjukkan bagaimana data cryptocurrency yang kompleks dapat diolah melalui suatu pipeline terstruktur menjadi sistem analitik yang informatif. Dashboard yang dihasilkan tidak hanya berfungsi sebagai alat visualisasi, tetapi juga sebagai sarana untuk membantu pengguna memahami kondisi pasar dan mendukung pengambilan keputusan yang lebih baik.
