iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
    {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
    {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
    {"codigo": "INI-004", "sector": "tecnologia"}
]


def seleccionar_pendientes(registros, sector):
    """
    Retorna los códigos del sector indicado
    con pendiente exactamente igual a True.
    """
    resultados = []

    for iniciativa in registros:
        if (
            iniciativa.get("sector") == sector
            and iniciativa.get("pendiente") is True
        ):
            resultados.append(iniciativa["codigo"])

    return resultados


# Prueba 1: debe encontrar resultados
resultado1 = seleccionar_pendientes(iniciativas, "tecnologia")

print("=== PRUEBA 1 ===")
print("Sector: tecnologia")
print("Resultado:", resultado1)


# Prueba 2: no debe encontrar resultados
resultado2 = seleccionar_pendientes(iniciativas, "salud")

print("\n=== PRUEBA 2 ===")
print("Sector: salud")
print("Resultado:", resultado2)