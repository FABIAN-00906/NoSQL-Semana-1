# Registro del entorno — Bases de Datos NoSQL

## 1. Información general

- **Sistema operativo:** Windows.
- **Terminal utilizada:** Git Bash (MINGW64).
- **Base de datos:** `emprendimiento_sena_lab`.
- **Dirección del servidor:** `127.0.0.1:27017`.
- **Usuario de práctica:** No configurado; la conexión local se realizó sin credenciales.
- **Autenticación:** Pendiente de verificar con las credenciales de práctica proporcionadas por el instructor.

## 2. Versiones de las herramientas

- **Python:** 3.14.7.
- **Git:** 2.55.0.windows.5.
- **MongoDB Shell (`mongosh`):** 2.13.0.
- **Servidor MongoDB:** 7.0.43.

## 3. Práctica realizada

Se ejecutó el script `scripts/01_explorar.js` para explorar un documento de asesoría en la colección `asesorias_demo` de la base `emprendimiento_sena_lab`.

Se verificaron el identificador `ASE-DEMO-001`, la cantidad de documentos asociados a ese identificador y el tipo de la fecha programada.

## 4. Resultados obtenidos

- **Conexión local:** correcta.
- **Comando `ping`:** respuesta `ok: 1`.
- **Documento consultado:** `ASE-DEMO-001`, encontrado correctamente.
- **Conteo de documentos para ese identificador:** `1`.
- **Comprobación `fecha_programada instanceof Date`:** `true`.
- **Colección utilizada:** `asesorias_demo`.

## 5. Dificultades y solución

Inicialmente se presentó una diferencia de sintaxis entre PowerShell y Git Bash al ejecutar comandos de Python. Se solucionó utilizando `py` para ejecutar Python desde Git Bash.

La conexión local a MongoDB funcionó sin solicitar credenciales. Sin embargo, esto no demuestra una conexión autenticada con la cuenta de práctica exigida en la guía.

## 6. Pendientes

- Verificar la conexión autenticada con la cuenta de práctica del instructor cuando se faciliten las credenciales.
- Guardar una captura de la ejecución del script como evidencia, si el instructor la solicita.
- Confirmar con el instructor que la configuración local sin credenciales se acepta como evidencia provisional.
