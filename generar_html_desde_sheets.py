import requests

# URL pública del HTML publicado desde Sheets
URL_SHEETS_HTML = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTnk86vrqjfLTuPW_-PJm86Ufk52R34oHWi_ESp2UwNjicjLQrMISqFQo7rntJ4H-Uy-AKOMzWgJPxM/pubhtml?gid=2122392688&single=true"

# Archivo de salida
ARCHIVO_SALIDA = "libros.html"

def descargar_html():
    print("📥 Descargando HTML desde Google Sheets…")

    r = requests.get(URL_SHEETS_HTML)

    if r.status_code == 200:
        with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
            f.write(r.text)
        print("✔ Catálogo actualizado correctamente en libros.html")
    else:
        print("❌ Error descargando HTML:", r.status_code)

if __name__ == "__main__":
    descargar_html()