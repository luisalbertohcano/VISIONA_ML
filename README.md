# VISIONA_ML

# VISIONA - Plataforma de Predicción de Peligrosidad

Este proyecto es una plataforma web desarrollada para predecir la peligrosidad de municipios basada en diversos factores como el número de habitantes, accidentes y víctimas. La interfaz está diseñada con HTML, CSS y Bootstrap, y utiliza un servidor backend en Flask para procesar los datos y generar las predicciones.

## Características

- Formulario interactivo para ingresar datos del municipio.
- Predicción de peligrosidad basada en los datos ingresados.
- Diseño responsivo y moderno utilizando Bootstrap.


## Tecnologías Utilizadas

- HTML
- CSS
- Bootstrap 4.5.2
- Flask (Python)

## Requisitos

- Python 3.x
- Flask
- Bootstrap (incluido en el HTML)

## Instalación

1. Clona el repositorio a tu máquina local:
    ```bash
    git clone https://github.com/tu_usuario/visiona-prediccion.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd visiona-prediccion
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv env
    ```
4. Activa el entorno virtual:
    - En Windows:
      ```bash
      .\env\Scripts\activate
      ```
    - En MacOS/Linux:
      ```bash
      source env/bin/activate
      ```
5. Instala las dependencias requeridas:
    ```bash
    pip install flask
    ```

## Uso

1. Coloca tu archivo de logo `visionalogo.png` en el directorio `static/images`.
2. Ejecuta la aplicación Flask:
    ```bash
    flask run
    ```
3. Abre tu navegador y navega a `http://127.0.0.1:5000` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

```plaintext
visiona-prediccion/
│
├── static/
│   └── images/
│       └── visionalogo.png
│
├── templates/
│   └── index.html
│
├── app.py
├── README.md
└── requirements.txt
