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
gas/                        # misma interfaz en una sola página para Google Apps Script
```

## Ejecutar
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.app
```
Abrir http://localhost:5000
