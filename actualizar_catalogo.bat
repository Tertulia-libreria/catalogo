@echo off
cd /d "C:\Users\W 10\Desktop\Enlace suma\catalogo\"

echo =========================================
echo === ACTUALIZANDO INVENTARIO Y CATALOGO ==
echo =========================================
echo.

echo [1/3] Ejecutando sync_suma.py ...
py "..\sync_suma.py"
if %errorlevel% NEQ 0 (
    echo ❌ Error en sync_suma.py
    pause
    exit /b
)
echo ✔ sync_suma.py completado.
echo.

echo [2/3] Generando libros.html desde Sheets ...
py generar_html_desde_sheets.py
if %errorlevel% NEQ 0 (
    echo ❌ Error generando HTML
    pause
    exit /b
)
echo ✔ HTML actualizado.
echo.

echo [3/3] Subiendo cambios a GitHub...
py subir_a_github.py
if %errorlevel% NEQ 0 (
    echo ❌ Error subiendo a GitHub
    pause
    exit /b
)

echo =========================================
echo ✔ PROCESO COMPLETO
echo =========================================
pause