# Evidencias A1 — Diagnóstico

Este archivo registra los resultados obtenidos al ejecutar los tres scripts del diagnóstico. Antes de entregar, vuelve a ejecutarlos en tu computador y confirma que las salidas coincidan con las registradas aquí.

## P1 — JSON

**Archivo ejecutado:** `diagnostico_nosql/P1_json.py`

La primera versión contiene un error intencional: utiliza `True` en lugar de `true` y deja una coma final en el arreglo. La lectura inicial informa un error de sintaxis JSON. En la versión corregida se utiliza `true` y se elimina la coma final.

**Salida obtenida al ejecutar el script:**

```text
=== VERSIÓN INICIAL ===
Error encontrado:
Expecting value: line 1 column 31 (char 30)

=== VERSIÓN CORREGIDA ===
Código: INI-001
Activa: True
Tipo de código: str
Tipo de activa: bool
```

**Conclusión:** `codigo` se interpreta como cadena (`str`) y `activa` como booleano (`bool`) en Python.

Estado: **Completado**.

---

## P2 — Python

**Archivo ejecutado:** `diagnostico_nosql/P2_python.py`

La función `seleccionar_pendientes(registros, sector)` devuelve los códigos que pertenecen al sector solicitado y cuyo campo `pendiente` es exactamente `True`. Cuando el campo no existe, `iniciativa.get("pendiente")` devuelve `None`, por lo que ese registro no se incluye. La función no modifica la lista original.

**Salida obtenida al ejecutar el script:**

```text
=== PRUEBA 1 ===
Sector: tecnologia
Resultado: ['INI-001']

=== PRUEBA 2 ===
Sector: salud
Resultado: []
```

**Conclusión:** la primera prueba encuentra `INI-001`. La segunda no encuentra coincidencias y devuelve una lista vacía. Se comprueba el booleano con `is True` para no confundirlo con otros valores, como la cadena `"True"`.

Estado: **Completado**.

---

## P3 — SQL

**Archivo ejecutado:** `diagnostico_nosql/P3_sql.py`

La consulta relaciona las tablas `iniciativas` y `emprendedores` mediante `iniciativas.emprendedor_id = emprendedores.id`. Filtra las iniciativas cuyo estado es `activa` y ordena el resultado por el identificador de la iniciativa.

**Salida obtenida al ejecutar el script:**

```text
=== INICIATIVAS ACTIVAS ===
(101, 'Emprendedor A')
(103, 'Emprendedor A')
```

**Conclusión:** se muestran las iniciativas activas 101 y 103 junto con el alias del emprendedor responsable. Ambas pertenecen a `Emprendedor A`.

Estado: **Completado**.

---

## Resumen de evidencias

| Componente | Archivo | Estado |
|---|---|---|
| P1 — JSON | `diagnostico_nosql/P1_json.py` | Completado |
| P2 — Python | `diagnostico_nosql/P2_python.py` | Completado |
| P3 — SQL | `diagnostico_nosql/P3_sql.py` | Completado |
| Preguntas teóricas | `diagnostico_nosql/diagnostico_teorico.md` | Completado |
| Autoevaluación | `diagnostico_nosql/diagnostico_teorico.md` | Completada |

## Pendiente antes de la entrega

- Volver a ejecutar los tres scripts desde la terminal del equipo.
- Guardar capturas de pantalla de las salidas, si el instructor las solicita.
- Registrar cualquier diferencia o dificultad real encontrada durante la ejecución.
