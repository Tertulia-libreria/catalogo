import requests
import subprocess
import datetime
import os

# ---------------- CONFIG ----------------
# URL pública del HTML publicado desde Sheets
URL_SHEETS_HTML = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTnk86vrqjfLTuPW_-PJm86Ufk52R34oHWi_ESp2UwNjicjLQrMISqFQo7rntJ4H-Uy-AKOMzWgJPxM/pubhtml?gid=2122392688&single=true"

# Archivo de salida dentro del repo local
ARCHIVO_SALIDA = "libros.html"

# Ruta del repositorio local de GitHub
RUTA_REPO = r"C:\Users\W 10\Desktop\Enlace suma\catalogo"
# ---------------------------------------

def descargar_html():
    """Descarga el HTML desde Google Sheets y lo guarda en el repo local."""
    print("🔄 Descargando HTML desde Google Sheets...")
    try:
        r = requests.get(URL_SHEETS_HTML)
        r.raise_for_status()  # Lanza error si hay fallo
    except Exception as e:
        print("❌ Error descargando HTML:", e)
        return False

    # Guardar archivo
    archivo_completo = os.path.join(RUTA_REPO, ARCHIVO_SALIDA)
    with open(archivo_completo, "w", encoding="utf-8") as f:
        f.write(r.text)

    print(f"✅ HTML guardado en {archivo_completo}")
    return True

def subir_github():
    """Hace git add, commit y push si hay cambios."""
    os.chdir(RUTA_REPO)
    print("📤 Comprobando cambios y subiendo a GitHub...")

    try:
        # Agregar cambios
        subprocess.run(["git", "add", "."], check=True)

        # Commit con fecha y hora
        mensaje = "Actualización automática del catálogo - " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado = subprocess.run(["git", "commit", "-m", mensaje], check=False)

        if resultado.returncode != 0:
            print("ℹ No hay cambios para subir.")
        else:
            subprocess.run(["git", "push"], check=True)
            print("✔ Catálogo subido correctamente a GitHub.")

    except subprocess.CalledProcessError as e:
        print("❌ Error durante el proceso Git:", e)

if __name__ == "__main__":
    if descargar_html():  # Solo sube si se descargó correctamente
        subir_github()