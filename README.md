📋 ClassCheckk

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
1-TANITIM:
<img width="1884" height="915" alt="bir" src="https://github.com/user-attachments/assets/75a97369-043f-44fd-8106-0f4588a410a6" />

2-GİRİŞ:
<img width="1911" height="904" alt="iki" src="https://github.com/user-attachments/assets/7a29db3d-e0d0-4726-a024-677e3f33293d" />

3-HOME:
<img width="1899" height="848" alt="uc" src="https://github.com/user-attachments/assets/68e25efb-cd3b-4757-b53a-9c3ad25ca6bf" />

4-ADD COURSE:
<img width="1914" height="914" alt="dort" src="https://github.com/user-attachments/assets/faf55cc4-3463-46f2-a5a9-880da858904a" />

5-DETAİL COURSE:
<img width="1851" height="866" alt="bes" src="https://github.com/user-attachments/assets/f64a8ce2-a135-4488-8448-c7777de4ce71" />

6-ADD STUDENT: 
<img width="1871" height="903" alt="alti" src="https://github.com/user-attachments/assets/6b4d34d2-11bc-4ecb-8cb2-1899d7960cf7" />

7-UPDATE COURSE:
<img width="1872" height="905" alt="yedi" src="https://github.com/user-attachments/assets/d166608d-c5d6-46c7-8c68-797e2e3b43eb" />

8-QR:
<img width="1726" height="829" alt="sekiz" src="https://github.com/user-attachments/assets/7e608a46-9782-4ccd-926d-773076f0bbc0" />

9-ATTENDANCE FORM:
<img width="944" height="839" alt="dokuz" src="https://github.com/user-attachments/assets/5fa35da4-164f-46b0-abd5-383b12c7cc17" />

10-ATTENDANCE RECORDED:
<img width="547" height="649" alt="on" src="https://github.com/user-attachments/assets/fe16f77a-c81e-4b5f-84bd-b5370ef60b35" />

11-ATTENDANCE LİST:
<img width="1738" height="435" alt="on bir" src="https://github.com/user-attachments/assets/636f45c2-6e64-4ba5-ba9c-4d2242aedf8b" />






## 🤝 Katkı

Pull request'ler kabul edilir. Büyük değişiklikler için önce bir issue açmanız önerilir.

---

## 📄 Lisans

[MIT](LICENSE)

---

<p align="center">Made with ❤️ by <a href="https://github.com/esmadenizerboga">esmadenizerboga</a></p>
