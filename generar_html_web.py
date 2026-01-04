import requests

WEBAPP_URL = "https://script.google.com/macros/s/AKfycby0I4zJSTM1bpWNB0QVpktidbyuXDzZFa1EjfZblZ0zwhkBrtAxYU45BQT88uHZhZYGPQ/exec"

print("=== DESCARGANDO HTML DESDE GOOGLE SHEETS ===")

r = requests.get(WEBAPP_URL, timeout=30)
r.raise_for_status()

html = r.text.strip()

with open("libros.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✔ HTML COMPLETO GUARDADO COMO libros.html")


