@echo off
echo === INICIANDO ACTUALIZACION ===

cd /d "%~dp0"

echo === EJECUTANDO SYNC SUMA ===
py sync_suma.py
if errorlevel 1 goto error

echo === GENERANDO HTML DESDE SHEETS ===
py generar_html_web.py
if errorlevel 1 goto error

echo === SUBIENDO A GITHUB ===
git add libros.html
git commit -m "Actualiza catálogo"
git push
if errorlevel 1 goto error

echo === ACTUALIZACION COMPLETA ===
pause
exit /b 0

:error
echo === ERROR EN EL PROCESO ===
pause
exit /b 1