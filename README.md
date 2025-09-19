# 📂 Aplikasi Arsip BWS Papua Barat

Aplikasi Arsip Internal untuk **Balai Wilayah Sungai Papua Barat (BWS PB)** di bawah **Kementerian Pekerjaan Umum dan Perumahan Rakyat (PUPR), Ditjen Sumber Daya Air**.  
Aplikasi ini digunakan untuk menyimpan, mengelola, dan mengakses dokumen pekerjaan fisik & non-fisik dalam bentuk **PDF**, berdasarkan paket pekerjaan dari masing-masing **PPK**, dan dapat diakses melalui **jaringan intranet**.

---

## ✨ Fitur Utama

- 📁 **Manajemen Arsip**
  - Upload, edit, hapus, dan unduh file PDF.
  - Klasifikasi berdasarkan paket pekerjaan, jenis pekerjaan, tahun, dan PPK.
- 🔎 **Pencarian & Filter**
  - Cari dokumen berdasarkan metadata.
  - Filter dokumen berdasarkan tahun, kategori, atau PPK.
- 🔐 **Manajemen Akses**
  - Role-based access (Admin / User).
  - Hak akses dokumen terbatas sesuai level pengguna.
- 📊 **Dashboard**
  - Statistik jumlah dokumen per kategori.
  - Ringkasan arsip per tahun.
- 🧾 **Fitur Tambahan (Opsional)**
  - QR Code untuk akses cepat dokumen.
  - Logging aktivitas user (upload, download, delete).
  - Backup otomatis ke **WD My Cloud PR4100**.

---

## 🏗️ Teknologi yang Digunakan

- **Backend:** Django / Django REST Framework
- **Frontend:** HTML, TailwindCSS (opsional: React untuk UI lebih interaktif)
- **Database:** MySQL / PostgreSQL
- **Storage:** File System (Media Root), WD My Cloud PR4100 (backup)
- **Server:** Apache / Nginx (intranet BWS PB)

---

## 🚀 Instalasi & Setup

1. **Clone repository**

   ```bash
   git clone https://github.com/username/arsip-bws.git
   cd arsip-bws
   ```

2. **Terminal**

   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\scripts\activate # Windows
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Run App**

   ```bash
   python manage.py runserver
   http://127.0.0.1:8000
   ```
