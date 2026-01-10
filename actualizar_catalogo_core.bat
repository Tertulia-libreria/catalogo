@echo off
REM =====================================
REM  ACTUALIZAR CATÁLOGO - PROCESO CENTRAL
REM =====================================

cd /d "%~dp0"

echo.
echo ================================
echo 🚀 INICIANDO ACTUALIZACIÓN
echo ================================
echo.

REM === SYNC SUMA ===
echo 🔄 Ejecutando sincronización con SUMA...
py sync_suma.py
if errorlevel 1 goto error
echo ✅ Inventario sincronizado correctamente
echo.

REM === GENERAR HTML ===
echo 🧩 Generando HTML completo desde Google Sheets...
py generar_html_web.py
if errorlevel 1 goto error
echo ✅ HTML generado correctamente (libros.html)
echo.

REM === GITHUB ===
echo ☁️ Subiendo cambios a GitHub...
git add libros.html
git commit -m "Actualiza catálogo"
git push
if errorlevel 1 goto error
echo ✅ Cambios subidos correctamente a GitHub
echo.

echo ================================
echo 🎉 ACTUALIZACIÓN COMPLETA
echo ================================
echo.

REM === TODO OK: CERRAR ===
exit /b 0

:error
echo.
echo ================================
echo ❌ ERROR EN EL PROCESO
echo ================================
echo Revisa el mensaje anterior para más detalles.
echo.
pause
exit /b 1