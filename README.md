# 📋 ClassCheckk

> **Django Based Multi-User Course Attendance Tracking System**

ClassCheckk is a web-based attendance management system that allows teachers to track student attendance via QR codes, manage courses, and generate reports — all from a mobile-friendly interface.

---

## ✨ Features

- 👥 **Multi-User Roles** — Separate dashboards and permissions for teachers, students, and admins
- 📱 **QR Code Attendance** — Students check in by scanning a unique QR code generated per class session
- 🛡️ **Admin Panel** — Full control over users, courses, and attendance records
- 📊 **Reporting** — View and track attendance history per student and course
- 📲 **Mobile Responsive** — Fully usable on phones and tablets via Bootstrap

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Repoyu klonla
git clone https://github.com/esmadenizerboga/ClassCheckk.git
cd ClassCheckk

# 2. Sanal ortam oluştur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. Veritabanını oluştur
python manage.py migrate

# 5. Admin kullanıcısı oluştur
python manage.py createsuperuser

# 6. Sunucuyu başlat
python manage.py runserver
```

Tarayıcıda `http://127.0.0.1:8000` adresini aç.

---

## 👤 Kullanıcı Rolleri

| Rol | Yetkiler |
|-----|----------|
| **Admin** | Tüm kullanıcıları, dersleri ve yoklamaları yönetir |
| **Öğretmen** | Ders oluşturur, QR kod üretir, yoklama görüntüler |
| **Öğrenci** | QR kodu tarayarak yoklamaya katılır |

---

## 📁 Proje Yapısı

```
ClassCheckk/
├── accounts/        # Kullanıcı yönetimi & roller
├── courses/         # Ders modelleri ve görünümleri
├── attendance/      # Yoklama mantığı & QR kod
├── templates/       # HTML şablonları
├── static/          # CSS, JS, görseller
└── manage.py
```

---

## 📸 Ekran Görüntüleri

> *(Buraya proje ekran görüntüleri eklenecek)*

---

## 🤝 Katkı

Pull request'ler kabul edilir. Büyük değişiklikler için önce bir issue açmanız önerilir.

---

## 📄 Lisans

[MIT](LICENSE)

---

<p align="center">Made with ❤️ by <a href="https://github.com/esmadenizerboga">esmadenizerboga</a></p>
