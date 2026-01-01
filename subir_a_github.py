import subprocess
import datetime
import os

# Ruta del repositorio local
RUTA_REPO = r"C:\Users\W 10\Desktop\Enlace suma\catalogo"

os.chdir(RUTA_REPO)
print("📤 Subiendo catálogo actualizado a GitHub…")

try:
    # git add
    subprocess.run(["git", "add", "."], check=True)

    # Mensaje con fecha y hora
    mensaje = "Actualización automática del catálogo - " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultado = subprocess.run(["git", "commit", "-m", mensaje], check=False)

    # Si no hay cambios no hagas push
    if resultado.returncode != 0:
        print("ℹ No hay cambios para subir.")
    else:
        subprocess.run(["git", "push"], check=True)
        print("✔ Catálogo subido correctamente a GitHub.")

except subprocess.CalledProcessError as e:
    print("❌ Error durante el proceso Git:")
    print(e)