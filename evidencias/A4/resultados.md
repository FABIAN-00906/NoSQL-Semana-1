# Evidencias A4 — Exploración de MongoDB

## Comandos ejecutados

```bash
mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" --file scripts/01_explorar.js
```

## Resultados observados

- El script encontró el documento `ASE-DEMO-001` en la colección `asesorias_demo`.
- El conteo para el identificador `ASE-DEMO-001` fue `1`.
- La expresión `asesoria.fecha_programada instanceof Date` devolvió `true`.
- El campo `fecha_programada` se mostró como `ISODate('2026-10-08T13:00:00.000Z')`.

## Interpretación de tipos

- `emprendedor_alias`: cadena de texto.
- `requiere_seguimiento`: booleano.
- `temas`: arreglo de cadenas.
- `iniciativa`: subdocumento con código, nombre y sector.
- `fecha_programada`: fecha BSON (`Date`).
- `fecha_realizacion`: valor nulo (`null`).

## Observación sobre autenticación

La prueba se realizó contra el servidor local sin introducir credenciales. Por tanto, demuestra conectividad y exploración del documento, pero **no demuestra la conexión autenticada** solicitada por la guía. Esta verificación queda pendiente de las credenciales de práctica del instructor.
