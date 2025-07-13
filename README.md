# Apache Airflow ETL Project 🛠️

Project ini berisi pipeline ETL menggunakan **Apache Airflow**, serta dilengkapi dengan pengujian menggunakan **pytest**, dan dijalankan dalam **Docker** environment.

## 📁 Struktur Folder
.
├── dags/ # Berisi DAG Airflow
│ ├── etl_pipeline.py
│ └── utils.py # Fungsi extract, transform, load
├── docker-compose.yml # File Docker untuk menjalankan Airflow
├── airflow.cfg # Konfigurasi Airflow (jika tidak menggunakan Docker)
├── requirements.txt # Daftar dependencies
├── tests/ # Folder test pytest
│ └── test_etl.py
├── .gitignore
└── README.md

## 🚀 Menjalankan dengan Docker

Pastikan Docker dan Docker Compose telah terinstal.

```bash
docker-compose up --build

## 🧪 Menjalankan Unit Test

```bash
pip install pytest
```

Lalu jalankan:

```bash
pip install pytest
```

## ⚙️ Tools yang Digunakan
- 🐍 **Python** – Core programming language
- 🌬️ **Apache Airflow** – Workflow orchestration tool
- 🐳 **Docker** – Containerization for environment consistency
- 🐘 **pgAdmin4 + PostgreSQL** – Database and GUI management
- 🐼 **Pandas** – Data manipulation and analysis
- 🧪 **Pytest** – Unit testing framework for Python
