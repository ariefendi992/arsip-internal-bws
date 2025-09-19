# Roadmap Aplikasi Arsip BWS

Aplikasi Arsip Internal Balai Wilayah Sungai Papua Barat (BWS PB)  
Tujuan: Menyimpan, mengelola, dan mengakses dokumen pekerjaan fisik & non-fisik dalam format PDF secara intranet.

---

## ✅ Tahap 1: Persiapan & Dasar

- [x] Inisialisasi repository GitHub & struktur project
- [x] Setup Django project (`config`, `apps.arsip`)
- [x] Konfigurasi database (MySQL)
- [ ] Setup static & media root untuk penyimpanan file
- [ ] Autentikasi user dasar (login/logout, role admin/user)

---

## 🔄 Tahap 2: Modul Arsip Dasar

- [ ] CRUD untuk data paket pekerjaan
- [ ] Upload PDF per paket (dibagi per PPK)
- [ ] Tampilan daftar dokumen (sortable & searchable)
- [ ] Metadata dokumen (judul, tahun, jenis, PPK)
- [ ] Hak akses dokumen (role-based)

---

## 🔄 Tahap 3: Pengelolaan & Fitur Tambahan

- [ ] Dashboard ringkasan jumlah dokumen per kategori
- [ ] Filter berdasarkan tahun, PPK, jenis pekerjaan
- [ ] QR Code untuk akses cepat file PDF di intranet
- [ ] Logging aktivitas user (upload, download, delete)

---

## 🚀 Tahap 4: Optimalisasi & Deployment

- [ ] Integrasi dengan server intranet (cPanel / Apache / Nginx)
- [ ] Optimasi kecepatan load file PDF
- [ ] Backup otomatis ke WD My Cloud PR4100
- [ ] Dokumentasi teknis (README, panduan admin & user)
- [ ] Testing internal & uji coba di BWS PB

---

## 🛠 Tahap 5: Pengembangan Lanjutan

- [ ] Single Sign-On (SSO) dengan akun internal Kementerian PU
- [ ] Notifikasi email/telegram jika ada dokumen baru
- [ ] API REST untuk akses arsip dari aplikasi lain
- [ ] Versi mobile-friendly (Flutter / PWA)
- [ ] Integrasi geotagging lokasi paket (opsional)

---

## 📌 Catatan

- Project ini hanya berjalan di jaringan **intranet BWS PB**.
- Dokumen bersifat **internal** dan tidak dipublikasikan ke publik.
- Roadmap ini fleksibel & bisa disesuaikan dengan kebutuhan lapangan.
