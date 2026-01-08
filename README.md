# Conversor de artículos web a audio (MP3)

## 🧩Objetivo del proyecto

Este proyecto permite convertir el texto de un artículo en la web en un archivo de audio en formato MP3, utilizando Python.  
El usuario ingresa la URL de una noticia o artículo y el programa descarga el contenido, lo procesa y genera un archivo de audio listo para reproducir.

---

## 🏗️Requisitos

- Python 3.10 o superior instalado en el sistema.  
- Acceso a internet (para descargar el artículo y usar gTTS).  
- Git (opcional, si clonas el repositorio).  

Dependencias principales del proyecto (se instalan con `requirements.txt`):

- `newspaper3k` – para descargar y extraer el texto del artículo.  
- `gTTS` – Google Text-to-Speech, para generar el audio MP3. 

---

## ⚙️ Configuración del ambiente

#### 1. Clonar el repositorio (opcional):
- git clone https://github.com/tu-usuario/proyecto_texto_a_audio.git
- cd proyecto_texto_a_audio

#### 2. Crear el entorno virtual:
- python -m venv venv
o según tu sistema
- python3 -m venv venv

#### 3. Activar el entorno virtual:
en linux:
- source venv/bin/activate

en Windows:
- venv\Scripts\activate

#### 4. Instalar dependencias desde requirements.txt:
Asegúrate de estar en la carpeta del proyecto, con el entorno virtual activado:
- pip install -r requirements.txt

#### 5. Ejecución del script
Con el entorno virtual activado y las dependencias instaladas:
- python main.py
o
- python3 main.py

---
## 💻Flujo de uso:

##### 1. El programa mostrará un banner en consola.

##### 2. Se solicitará ingresar la URL del artículo (HTTP o HTTPS).

    - Puedes escribir una URL válida (por ejemplo, de un diario o portal de noticias).

    - Puedes escribir "S" para salir del programa.

##### 3. El programa descargará y procesará el artículo.

##### 4. Si el texto es suficiente, se generará un archivo MP3 en la carpeta del proyecto.

 - El nombre del archivo se construye a partir del título del artículo, limpio y truncado a 10 caracteres, con extensión .mp3.

##### 5. Al finalizar, el programa preguntará si deseas convertir otro artículo.
---

## 📚 Recursos recomendados
Para aprender y profundizar en los temas usados en este proyecto:

- [Entornos virtuales y paquetes en Python](https://docs.python.org/3/tutorial/venv.html)

- [Uso de venv para crear entornos virtuales](https://docs.python.org/3/library/venv.html)

- [Instalación de dependencias con requirements.txt](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

- [Newspaper3k (extracción de artículos)](https://pypi.org/project/newspaper3k/)

- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)

---

## ✍️ Autoría y comunidad
Este repo forma parte de mi proceso de aprendizaje en desarrollo fullstack, adicionalmente está pensado para compartir con la comunidad (Conquer o quien lo necesite).

Si te sirve:
- Puedes abrir Issues con dudas o mejoras.
- Puedes hacer Pull Requests con mejoras al script, documentación, etc
- Sugerencias de contribución:
    - Limpieza y preprocesamiento extra del texto.
    - Soporte para otros idiomas además de español. 
    - Logs de actividad en archivo (URL, fecha, archivo generado).



<!-- Python --> <img src="https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54" alt="Python" />

![SO](https://img.shields.io/badge/SO-Linux%20-lightgrey)
![Protocolo](https://img.shields.io/badge/protocolo-HTTP%20%7C%20HTTPS-orange)



