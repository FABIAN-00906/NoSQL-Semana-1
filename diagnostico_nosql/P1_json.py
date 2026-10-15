import json

# Versión inicial con error
texto = '{"codigo":"INI-001", "activa":True, "intereses":["Validar mercado",]}'

print("=== VERSIÓN INICIAL ===")

try:
    datos = json.loads(texto)
    print(datos)
except json.JSONDecodeError as error:
    print("Error encontrado:")
    print(error)


# Versión corregida
texto_corregido = '{"codigo":"INI-001", "activa":true, "intereses":["Validar mercado"]}'

print("\n=== VERSIÓN CORREGIDA ===")

datos = json.loads(texto_corregido)

print("Código:", datos["codigo"])
print("Activa:", datos["activa"])
print("Tipo de código:", type(datos["codigo"]).__name__)
print("Tipo de activa:", type(datos["activa"]).__name__)