🧪 Proyecto de Automatización con Selenium y Python

📌 Propósito del proyecto

Este proyecto automatiza pruebas funcionales sobre la aplicación Sauce Demo utilizando Selenium WebDriver y Pytest bajo el patrón Page Object Model (POM).
El objetivo es validar funcionalidades clave como:

- Inicio de sesión (login)

- Visualización del catálogo

- Validación de precios y nombres de productos

- Agregado de productos al carrito

- Verificación del contador del carrito

Este repositorio se creó como práctica profesional aplicando conceptos aprendidos en el curso de automatización de Buenos Aprende.

🛠️ Tecnologías utilizadas

- Python 

- Pytest

- Selenium WebDriver

- Pytest-HTML (reportes)

- Page Object Model (POM)

📂 Estructura del proyecto
```
PROYECTO/
│
├── data/                      # Datos externos para pruebas
│   ├── data_login.csv
│   ├── data_login.json
│   └── data_login.py
│
├── page/                      # Implementación del Page Object Model
│   ├── cart_page.py
│   ├── checkout_complete_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── reports/                   # Reportes HTML generados por Pytest
│
├── screenshots/               # Capturas automáticas de fallos
│
├── test/                      # Pruebas automatizadas
│   ├── conftest.py
│   ├── test_cart_page.py
│   ├── test_checkout_complete_page.py
│   ├── test_checkout_page.py
│   ├── test_inventory_page.py
│   └── test_login_page.py
│
└── utils/                     # Utilidades y helpers
    ├── faker.py
    ├── helpers.py
    └── example.csv
```
📥 Instalación de dependencias

1- Cloná el repositorio:

git clone https://github.com/usuario/nombre-proyecto.git
cd nombre-proyecto

2- Instalar dependencias:

pip install -r requirements.txt

▶️ Ejecución de las pruebas
- Ejecución básica:
pytest

- Ejecución con más detalle:
pytest -v

- Ejecución generando reporte HTML:
pytest --html=reports/reporte.html --self-contained-html


Esto crea un archivo HTML dentro de reports/ que puede abrirse en cualquier navegador.

📸 Capturas automáticas de fallos

En este proyecto, cuando una prueba falla, se guarda automáticamente una captura en la carpeta screenshots/.

El comportamiento se maneja desde conftest.py:

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"screenshots/{item.name}.png")

📊 ¿Cómo interpretar los reportes HTML?

Al ejecutar:

pytest --html=reports/reporte.html --self-contained-html


El archivo generado incluye:

✔️ Tests pasados

❌ Tests fallados

🕒 Duración de cada prueba

📝 Logs y tracebacks

📷 Capturas (en caso de fallos, si las implementaste)

Simplemente abrí el archivo reporte.html en el navegador.
