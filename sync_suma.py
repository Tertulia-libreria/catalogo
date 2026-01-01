import sqlite3
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# -------------------------------------
# CONFIGURACIÓN
# -------------------------------------
ruta_sqlite = r"C:\Program Files (x86)\Suma Punto de Venta\Suma Punto de Venta\SQLiteSuma.db"
ruta_credenciales = r"enlace-suma-sheets-14eb650c31a8.json"
sheet_id = "1zbbNAIZ8NIGizU0WxNAESx9vL5vUSbJZOUaop3P4Dow"
sheet_name = "Hoja 1"

# -------------------------------------
# 1. LEER BASE DE DATOS SQLITE
# -------------------------------------

conn = sqlite3.connect(ruta_sqlite)

query = """
SELECT 
  p.ProductName AS titulo,
  p.Code AS code,
  p.Price AS precio,
  p.Existence AS existencia,
  t.ProductTypeName AS categoria
FROM product p
LEFT JOIN productType t ON p.ProductTypeId = t.Id
WHERE p.Active = 1
"""

df = pd.read_sql_query(query, conn)
conn.close()

df = df.fillna("")
df_final = df[["titulo", "precio", "categoria", "code", "existencia"]]

# -------------------------------------
# 2. CONECTAR A GOOGLE SHEETS
# -------------------------------------

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(ruta_credenciales, scopes=scopes)
service = build("sheets", "v4", credentials=creds)

# -------------------------------------
# 3. BORRAR DATOS ANTERIORES
# -------------------------------------

service.spreadsheets().values().clear(
    spreadsheetId=sheet_id,
    range=f"{sheet_name}!A:Z"
).execute()

# -------------------------------------
# 4. ESCRIBIR DATOS NUEVOS
# -------------------------------------

values = [df_final.columns.tolist()] + df_final.values.tolist()

service.spreadsheets().values().update(
    spreadsheetId=sheet_id,
    range=f"{sheet_name}!A1",
    valueInputOption="RAW",
    body={"values": values}
).execute()

print("✔ Inventario actualizado correctamente desde SUMA → Google Sheets → GitHub.")