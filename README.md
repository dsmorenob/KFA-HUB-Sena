# KFA HUB

Front-end de KFA HUB hecho con **Flask** y **Bootstrap 5.3**, siguiendo la estructura del proyecto
[ADSO-25T4-FacturApp_FrontEnd](https://github.com/jlballesterosv/ADSO-25T4-FacturApp_FrontEnd).

## Módulos
- **Horarios y precios** (`/list_schedules`)
- **Agenda una clase** (`/form_classes`)
- **Inscribirme** (`/form_enrollments`)

Los formularios aún no envían datos a ningún lado (solo front-end).

## Estructura
```
src/
├── app.py                  # punto de entrada
├── __init__.py             # create_app() y registro de Blueprints
├── controllers/            # un controller (Blueprint) por módulo
└── templates/              # layout.html + una carpeta por módulo
gas/                        # versión para Google Apps Script
```

## Versión en línea (Google Apps Script)

Instructor, la carpeta `gas/` contiene la misma interfaz en una sola página, publicada con Google Apps Script para poder abrirla desde cualquier dispositivo, sin instalar nada, de este modo puedo hacer pruebas con amigos:

https://script.google.com/macros/s/AKfycbxgiR6ujRXCNQ26jM9taZoqAQfTDHk8gYMHCtTLF30QHjBmXh_ShR4Pr3uBxc692vkxjQ/exec

La versión de Flask (`src/`) es la que corresponde al trabajo de la clase.

## Ejecutar

Intructor, este proyecto del sena lo estoy desarrollando en un servidor con **Linux (CasaOS)**, por eso en los comandos de abajo uso `source .venv/bin/activate`. En **Windows** el comando para activar el entorno virtual es distinto, como usted bien sabe: `.venv\Scripts\activate`.

### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.app
```

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.app
```

Luego abrir `http://localhost:5000` en el navegador.
