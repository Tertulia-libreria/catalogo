import requests

URL_HTML_SHEETS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTnk86vrqjfLTuPW_-PJm86Ufk52R34oHWi_ESp2UwNjicjLQrMISqFQo7rntJ4H-Uy-AKOMzWgJPxM/pub?output=html"

def descargar_html_desde_sheets():
    print("📥 Descargando HTML desde Google Sheets…")
    response = requests.get(URL_HTML_SHEETS)
    response.encoding = "utf-8"

    with open("libros.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("✔ Catálogo actualizado correctamente en libros.html")

if __name__ == "__main__":
    descargar_html_desde_sheets()