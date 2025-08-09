# Gym Inventory Project 🏋️‍♂️

Este proyecto es una aplicación web completa para gestionar el inventario de un gimnasio, desarrollada con:

- 📦 **Backend**: FastAPI (Python)
- 🌐 **Frontend**: HTML, CSS y JavaScript
- 🛢️ **Base de datos**: MySQL
- ⚙️ **ETL Pipeline**: Script en Python + cron
- 📁 **Backups**: Archivos CSV y logs JSON

---

## 🚀 Estructura del Proyecto

```
gym_inventory_project/
│
├── backend/
│   ├── main.py                  # App FastAPI principal
│   ├── routes/
│   │   ├── inventory.py         # Endpoints para obtener inventario limpio
│   │   └── pipeline.py          # Endpoint para correr el pipeline ETL
│   └── pipeline/
│       └── etl.py               # Script ETL (Extract, Transform, Load)
│
├── frontend/
│   └── index.html               # Interfaz web que consume datos limpios
│
├── sql/
│   └── schema.sql               # Script para crear base de datos y tablas
│
├── backups/                     # Carpeta donde se guardan respaldos
│
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
└── run.sh                       # Script para iniciar el backend
```

---

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone <repo-url>
cd gym_inventory_project
```

### 2. Crear la base de datos en MySQL

```bash
mysql -u root -p < sql/schema.sql
```

### 3. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Ejecutar el backend

```bash
bash run.sh
```

Accede a: [http://localhost:8000/docs](http://localhost:8000/docs) para ver la API.

---

## 🧪 Correr el pipeline manualmente

```bash
curl http://localhost:8000/api/pipeline/run
```

---

## 🧼 Qué hace el ETL

- Lee los datos de la tabla `inventory_raw`
- Limpia datos inválidos (cantidades negativas, nombres vacíos)
- Guarda los datos limpios en `inventory_cleaned`
- Genera backups CSV y logs JSON en la carpeta `backups`

---

## 🖥️ Frontend

Abre el archivo `frontend/index.html` en tu navegador para visualizar los datos limpios.

---

## 🧩 Autor

Proyecto creado por Luis Rojas para el curso de Programación Web (Entrega Grupal #4)
