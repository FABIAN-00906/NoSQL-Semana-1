# Diagnóstico teórico — A1

## 1. ¿Qué representan una tabla, una fila y una clave primaria? Utiliza un ejemplo relacionado con las iniciativas de emprendimiento.

Una tabla organiza información relacionada en filas y columnas. Una fila representa un registro individual y una clave primaria identifica de manera única cada registro.

Por ejemplo, una tabla de iniciativas podría ser:

| id | codigo | sector |
|---:|---|---|
| 1 | INI-001 | tecnologia |
| 2 | INI-002 | alimentos |

En este caso, `id` puede funcionar como clave primaria porque identifica de manera única cada fila.

---

## 2. ¿Para qué sirve una clave foránea? ¿Qué problema genera una iniciativa que referencia a un emprendedor inexistente?

Una clave foránea permite relacionar un registro con otro registro de una tabla diferente. Por ejemplo, `iniciativas.emprendedor_id` puede hacer referencia a `emprendedores.id`.

Si una iniciativa referencia a un emprendedor inexistente, se genera un problema de integridad referencial, porque la iniciativa quedaría asociada a un responsable que no existe.

---

## 3. Explica qué devuelve `SELECT codigo FROM iniciativas WHERE sector = 'tecnologia';`. ¿Modifica registros?

La consulta devuelve los códigos de las iniciativas cuyo sector sea `tecnologia`. Por ejemplo, podría devolver:

```text
INI-001
INI-003
INI-007
```

Es una consulta de lectura (`SELECT`), por lo que no modifica los registros.

---

## 4. Diferencia una lista y un diccionario en Python. ¿Qué estructura utilizarías para una iniciativa y para varias iniciativas?

Una lista almacena varios elementos en una secuencia:

```python
iniciativas = ["INI-001", "INI-002", "INI-003"]
```

Un diccionario almacena información mediante pares de clave y valor:

```python
iniciativa = {
    "codigo": "INI-001",
    "sector": "tecnologia"
}
```

Para representar una iniciativa utilizaría un diccionario. Para representar varias iniciativas utilizaría una lista de diccionarios:

```python
iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia"},
    {"codigo": "INI-002", "sector": "alimentos"}
]
```

---

## 5. ¿Son equivalentes `false` y `"false"` en JSON? Explica el tipo de cada valor.

No son equivalentes. `false` es un valor booleano, mientras que `"false"` es una cadena de texto. Por lo tanto, representan tipos de datos diferentes.

---

## 6. Diferencia un campo ausente, un campo con `null` y un campo con una cadena vacía. Propón un ejemplo.

Un campo ausente significa que la clave no existe en el documento:

```json
{
  "codigo": "INI-001"
}
```

Un campo con `null` significa que la clave existe, pero su valor es nulo:

```json
{
  "fecha_realizacion": null
}
```

Una cadena vacía significa que el campo existe y contiene texto de longitud cero:

```json
{
  "observacion": ""
}
```

Estas situaciones son diferentes y deben interpretarse según las reglas definidas para los datos.

---

## 7. ¿Qué ventaja tiene una función que retorna datos frente a otra que únicamente los imprime?

Una función que retorna datos permite que el resultado sea utilizado posteriormente por otras partes del programa.

```python
def obtener_codigo():
    return "INI-001"

codigo = obtener_codigo()
print(codigo)
```

En cambio, una función que solamente utiliza `print()` muestra el resultado, pero no lo entrega directamente para que otro proceso pueda utilizarlo.

---

## 8. Si falla la lectura de un archivo JSON, ¿qué revisarías antes de cambiar el programa?

Primero revisaría:

1. Que la ruta del archivo sea correcta.
2. Que el archivo exista.
3. Que el contenido tenga una sintaxis JSON válida.
4. Que se utilicen comillas dobles en las claves y cadenas.
5. Que los valores booleanos sean `true` o `false` en minúscula.
6. Que no existan comas finales incorrectas.
7. El mensaje exacto de la excepción.

Antes de modificar el programa, se debe identificar la causa del error.

---

## 9. ¿Qué información reconoces en `2026-10-06T13:00:00Z`? ¿Qué ambigüedades evita frente a `06/10/26 8:00`?

`2026-10-06T13:00:00Z` representa un instante de tiempo en formato ISO 8601. Sus partes son:

- `2026-10-06`: fecha.
- `13:00:00`: hora.
- `Z`: indica que la hora está expresada en UTC.

Este formato evita ambigüedades sobre el orden de la fecha y la zona horaria. Según la guía, este instante corresponde a las 08:00 en Colombia.

---

## 10. Se publicó por error una contraseña en Git. ¿Qué acciones propondrías? ¿Es suficiente borrarla del archivo actual?

Primero se debe considerar la contraseña como comprometida. Las acciones recomendadas son:

1. Cambiar o revocar inmediatamente la contraseña.
2. Revisar dónde fue expuesta.
3. Eliminarla del código actual.
4. Revisar el historial del repositorio y corregir la exposición según el procedimiento del responsable.
5. Revisar los accesos relacionados.
6. Utilizar variables de entorno o mecanismos seguros para las credenciales.
7. Verificar que `.gitignore` ayude a evitar publicar nuevamente secretos.

No es suficiente borrarla solamente del archivo actual, porque la contraseña puede permanecer en el historial de Git.

---

## Autoevaluación

### Puedo realizar...

- Identificar los conceptos básicos de tablas, filas, claves primarias y claves foráneas.
- Diferenciar listas y diccionarios en Python.
- Reconocer tipos de datos básicos en JSON.
- Identificar diferencias entre campos ausentes, `null` y cadenas vacías.
- Realizar filtros básicos utilizando Python.
- Realizar consultas SQL sencillas y relacionar tablas mediante `JOIN`.
- Interpretar fechas en formato ISO 8601.
- Reconocer la importancia de proteger las credenciales en Git.

### Necesito reforzar...

- El diseño y modelado de bases de datos NoSQL.
- Las consultas y relaciones entre datos.
- El manejo de documentos y colecciones en MongoDB.
- Las diferencias entre las familias de bases de datos NoSQL.

### Mi primera acción de mejora será...

Practicar los conceptos de bases de datos NoSQL y realizar ejercicios con MongoDB para comprender mejor los documentos, las colecciones, los tipos de datos y las consultas.

---

## Estado del diagnóstico

- P1 — JSON: completado.
- P2 — Python: completado.
- P3 — SQL: completado.
- Diagnóstico teórico: completado.
- Autoevaluación: completada.
