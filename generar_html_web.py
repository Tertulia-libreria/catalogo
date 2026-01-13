import requests

WEBAPP_URL = "https://script.google.com/macros/s/AKfycby0I4zJSTM1bpWNB0QVpktidbyuXDzZFa1EjfZblZ0zwhkBrtAxYU45BQT88uHZhZYGPQ/exec"

# ===== GOOGLE ANALYTICS =====
ANALYTICS = """
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-F9HV4XFVCH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-F9HV4XFVCH');
</script>
"""

print("=== DESCARGANDO HTML DESDE GOOGLE SHEETS ===")

r = requests.get(WEBAPP_URL, timeout=30)
r.raise_for_status()

html = r.text.strip()

# ===== INSERTAR ANALYTICS ANTES DE </head> =====
if "</head>" in html:
    html = html.replace("</head>", ANALYTICS + "\n</head>")
    print("✔ Google Analytics insertado correctamente")
else:
    print("⚠ No se encontró </head>, Analytics NO insertado")

# ===== GUARDAR HTML FINAL =====
with open("libros.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✔ HTML COMPLETO GUARDADO COMO libros.html")