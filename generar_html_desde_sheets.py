from __future__ import print_function
import os
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# ID de tu hoja:
SPREADSHEET_ID = "1zbbNAIZ8NIGizU0WxNAESx9vL5vUSbJZOUaop3P4Dow"

# Archivo donde se guardará el HTML
OUTPUT_FILE = "libros.html"

def obtener_html_desde_sheets():
    creds = Credentials.from_service_account_file(
        r"..\enlace-suma-sheets-14eb650c31a8.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )

    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    
    # LEER TODAS LAS FILAS DE LA HOJA HTML
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range="HTML!A:A"   # TODA LA COLUMNA
    ).execute()

    values = result.get("values", [])

    html_completo = ""
    for fila in values:
        if fila:               # evita filas vacías
            html_completo += fila[0]

    return html_completo


def guardar_html(html):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    print("📥 Descargando HTML desde Google Sheets...")
    html = obtener_html_desde_sheets()
    guardar_html(html)
    print("✔ Catálogo actualizado correctamente en libros.html")