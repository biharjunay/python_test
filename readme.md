# 🧪 Test Junior Programmer – FastPrint

## 📖 Pendahuluan

Repository ini berisi source code aplikasi **Tes Junior Programmer FastPrint** yang dikembangkan menggunakan **Django Framework**. Aplikasi ini bertujuan untuk mengambil data produk dari API FastPrint, menyimpannya ke dalam database relasional, serta menyajikannya dalam bentuk halaman web dan REST API.

Project ini dibuat sebagai bagian dari proses seleksi dan menunjukkan pemahaman dasar mengenai:
- Konsumsi API eksternal
- Pengolahan dan penyimpanan data
- Relasi database
- CRUD menggunakan Django
- REST API menggunakan Django REST Framework

---

## 🎯 Tujuan Aplikasi

Tujuan utama dari aplikasi ini adalah:
1. Mengambil data produk dari API FastPrint menggunakan autentikasi dinamis
2. Menyimpan data produk, kategori, dan status ke database
3. Menampilkan hanya produk dengan status **"bisa dijual"**
4. Menyediakan fitur manajemen data produk (CRUD)
5. Menyediakan endpoint API dalam format JSON

---

## ✨ Fitur Aplikasi

- ✅ Import data produk dari API FastPrint
- ✅ Penyimpanan data ke database MySQL
- ✅ Relasi antar tabel (Produk, Kategori, Status)
- ✅ Menampilkan produk dengan status "bisa dijual"
- ✅ Tambah, edit, dan hapus produk
- ✅ Validasi form input
- ✅ Konfirmasi sebelum menghapus data
- ✅ REST API endpoint

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Keterangan |
|---------|------------|
| Python | Versi 3.13 |
| Django | Versi 4.2 |
| Django REST Framework | API layer |
| MySQL | Database utama |
| HTML | Tampilan frontend |
| Django Template | Template engine |
| Requests | HTTP client |

---

## 📂 Struktur Folder Project

```
myproject/
│
├── api/                       # Django App utama
│   ├── __pycache__/
│   ├── migrations/            # File migrasi database
│   ├── templates/             # Template HTML
│   │   └── api/
│   │       ├── produk_list.html
│   │       └── produk_form.html
│   ├── __init__.py
│   ├── admin.py               # Konfigurasi Django Admin
│   ├── apps.py                # Konfigurasi App
│   ├── forms.py               # Django Form & validasi
│   ├── models.py              # Model database
│   ├── serializers.py         # Serializer REST API
│   ├── services.py            # Logic import API FastPrint
│   ├── tests.py               # Unit test (opsional)
│   ├── urls.py                # Routing app api
│   └── views.py               # View web & API
│
├── myproject/                 # Project utama Django
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Konfigurasi project
│   ├── urls.py                # Routing utama
│   └── wsgi.py
│
├── manage.py                  # Django CLI
└── README.md                  # Dokumentasi project
```

---

## 🗃️ Desain Database

### 📦 Tabel Produk

| Field | Tipe Data | Keterangan |
|------|----------|------------|
| id_produk | AutoField | Primary Key |
| nama_produk | CharField | Nama produk |
| harga | DecimalField | Harga produk |
| kategori | ForeignKey | Relasi ke tabel Kategori |
| status | ForeignKey | Relasi ke tabel Status |

### 🗂️ Tabel Kategori

| Field | Tipe Data | Keterangan |
|------|----------|------------|
| id_kategori | AutoField | Primary Key |
| nama_kategori | CharField | Nama kategori |

### 🚦 Tabel Status

| Field | Tipe Data | Keterangan |
|------|----------|------------|
| id_status | AutoField | Primary Key |
| nama_status | CharField | Status produk |

---

## 🔗 API FastPrint

**Endpoint API:**
```
https://recruitment.fastprint.co.id/tes/api_tes_programmer
```

### 🔐 Mekanisme Autentikasi

1. Username diperoleh dari response header:
   ```
   X-Credentials-Username
   ```
2. Password dibuat secara dinamis menggunakan format:
   ```
   bisacoding-{tanggal}-{bulan}-{2 digit tahun}
   ```
3. Password dienkripsi menggunakan algoritma **MD5**

---

## ⚙️ Instalasi & Menjalankan Aplikasi

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

### 2️⃣ Buat Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependency

```bash
pip install django djangorestframework requests mysqlclient
```

### 4️⃣ Konfigurasi Database

Sesuaikan konfigurasi database MySQL pada file `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fastprint_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Jalankan Server

```bash
python manage.py runserver
```

Akses aplikasi melalui browser:
```
http://localhost:8000/produk/
```

---

## 📥 Import Data dari API FastPrint

Data produk diambil dari API FastPrint menggunakan service khusus.

Masuk ke Django shell:

```bash
python manage.py shell
```

Jalankan perintah:

```python
from api.services import import_produk
import_produk()
```

---

## 🌐 Endpoint Aplikasi

### 🌍 Web Interface

| URL | Deskripsi |
|----|-----------|
| /produk/ | Menampilkan daftar produk |
| /produk/add/ | Menambah produk |
| /produk/edit/<id>/ | Mengedit produk |
| /produk/delete/<id>/ | Menghapus produk |

### 🔌 REST API Endpoint

| Method | URL | Keterangan |
|-------|-----|------------|
| GET | /api/produk/ | List produk (JSON) |

---

## ✅ Validasi & Keamanan

- Nama produk wajib diisi
- Harga harus berupa angka
- Konfirmasi sebelum menghapus data

---

## 📤 Pengumpulan Tes

1. Upload project ke GitHub pribadi
2. Kirim link repository ke:
   - prog3.fastprintsby@gmail.com
   - adm.hrdfastprint@gmail.com
3. Subject email:
   ```
   Test Programmer - Yusuf Biharjuna
   ```

---

## 👤 Author

- **Nama**: Yusuf Biharjuna
- **Posisi**: Junior Programmer
- **Framework**: Django
- **Tahun**: 2026

