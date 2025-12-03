import os
import datetime
import pytest
import pytest_html
from utils.helpers import get_driver

# Carpeta donde se guardarán las capturas
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    - Si el test falla:
        * Saca un screenshot
        * Lo guarda con nombre: nombreTest_YYYYMMDD_HHMMSS.png
        * Lo adjunta al reporte HTML (pytest-html)
    """
    outcome = yield
    report = outcome.get_result()

    # Lista de "extras" que se mostrarán en el reporte HTML
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed and not hasattr(report, "wasxfail"):
        driver = item.funcargs.get("driver", None)

        if driver is not None:
            test_name = item.name
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            file_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.join(SCREENSHOT_DIR, file_name)

            # 1) Guardar screenshot en el disco
            driver.save_screenshot(file_path)
            print(f"\n[SCREENSHOT] Captura guardada: {file_path}")

            # 2) Adjuntar screenshot al reporte HTML
            extras.append(
                pytest_html.extras.image(
                    file_path,
                    name=f"Screenshot - {test_name}"
                )
            )

    report.extras = extras
