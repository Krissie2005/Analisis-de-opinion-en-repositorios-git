# 📊 Análisis de Opinión en Repositorios Git


## 📌 Objetivo del proyecto

Este proyecto tiene como objetivo aplicar técnicas de Procesamiento de Lenguaje Natural (PLN) y Machine Learning para analizar mensajes extraídos de repositorios de GitHub.

Se busca:

* Identificar el sentimiento predominante (positivo, negativo o neutral).

* Detectar temas principales mediante agrupamiento.

* Medir la similitud semántica entre mensajes.

* Analizar el comportamiento de la comunidad en proyectos de software reales.

El análisis se realizó sobre los repositorios:

* auto1111_webui
* ytdlp

## 🧠 Descripción general del sistema

El sistema implementa un flujo completo de análisis textual:

- 🔎 Recolección automática de issues y comentarios desde la API de GitHub.

- 🧹 Limpieza y preprocesamiento del texto.

- 🔢 Representación vectorial mediante TF-IDF.

- 😊 Clasificación de sentimiento (modelo supervisado + enfoque léxico).

- 🧩 Identificación de temas con K-Means.

- 📐 Cálculo de similitud coseno entre mensajes.

Todo el proceso está organizado de forma modular en notebooks y funciones reutilizables.

## 📂 Estructura del repositorio

```text
ANALISIS DE OPINION EN REPOSITORIOS GIT
│
├── .vscode/
│   └── settings.json
│
├── data/
│   ├── auto1111_webui/
│   └── ytdlp/
│
├── notebooks/
│   ├── 01_recoleccion_datos.ipynb
│   ├── 02_preprocesamiento.ipynb
│   ├── 03_tfidf.ipynb
│   ├── 04_sentimiento.ipynb
│   ├── 05_temas.ipynb
│   └── 06_similitud.ipynb
│
├── src/
│   ├── __init__.py
│   └── sentiment_utils.py
│              
├── .env  # Variables de entorno (token GitHub)
├── .gitignore
└── README.md
```

## 🛠 Tecnologías utilizadas

- Lenguaje: Python

- Procesamiento de datos: Pandas, NumPy

- NLP: Scikit-learn (TF-IDF, K-Means, clasificación)

- Métricas: classification_report

- Similitud: cosine_similarity

- Gestión de entorno: .env

# ⚙️ Instrucciones para ejecución
###  1️⃣ Clonar el repositorio

```
git clone https://github.com/tu-usuario/tu-repositorio.git
cd ANALISIS-DE-OPINION-EN-REPOSITORIOS-GIT
```

### 2️⃣ Crear archivo .env

Agregar tu token personal de GitHub:

```
GITHUB_TOKEN=tu_token_aqui
```
### 3️⃣ Ejecutar notebooks

Abrir Jupyter Notebook o VS Code y ejecutar en orden:

* 01_recoleccion_datos

* 02_preprocesamiento

* 03_tfidf

* 04_sentimiento

* 05_temas

* 06_similitud
