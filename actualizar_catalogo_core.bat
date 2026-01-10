@echo off
title Actualización de Catálogo
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

git diff --cached --quiet
if %errorlevel%==0 (
  echo No hay cambios que subir.
  exit /b 0
)

git commit -m "Actualiza catálogo"
git push

echo === ACTUALIZACION COMPLETA ===
exit /b 0

:error
echo.
echo ======================================
echo ❌ ERROR EN EL PROCESO
echo ======================================
echo.
pause
exit /b 1