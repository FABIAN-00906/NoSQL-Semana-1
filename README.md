# Bases de Datos NoSQL — Semana 1

**Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) — SENA, CTMA Antioquia  
**Caso de estudio:** Unidad de Emprendimiento del SENA  
**Actividad:** Diagnóstico y fundamentos de bases de datos NoSQL

## 1. Objetivo

Organizar las evidencias de la Semana 1, diagnosticar conocimientos previos de Python, JSON y SQL, comparar familias de bases de datos y explorar un documento en MongoDB usando datos ficticios.

> Este proyecto es un ejercicio didáctico. Los registros de emprendedores e iniciativas son ficticios y no deben reemplazarse por datos personales o empresariales reales.

## 2. Estructura del proyecto

```text
NoSQL_Semana_1/
├── .gitignore
├── README.md
├── diagnostico_nosql/
│   ├── diagnostico_teorico.md
│   ├── P1_json.py
│   ├── P2_python.py
│   └── P3_sql.py
├── docs/
│   ├── matriz_A2.md
│   ├── consultas_A3.md
│   └── entorno.md
├── scripts/
│   └── 01_explorar.js
└── evidencias/
    ├── A1/
    │   └── resultados.md
    └── A4/
        └── resultados.md
```

## 3. Requisitos utilizados

- Windows y terminal Git Bash (MINGW64).
- Python 3.14.7, invocado con el comando `py`.
- Git 2.55.0.windows.5.
- MongoDB Shell (`mongosh`) 2.13.0.
- Servidor MongoDB 7.0.43.

Las versiones anteriores corresponden al entorno registrado para esta práctica; pueden variar en otros equipos.

## 4. Ejecutar el diagnóstico A1

Abre una terminal en la carpeta raíz `NoSQL_Semana_1` y ejecuta cada archivo por separado:

```bash
py diagnostico_nosql/P1_json.py
py diagnostico_nosql/P2_python.py
py diagnostico_nosql/P3_sql.py
```

Las salidas y explicaciones registradas están en `evidencias/A1/resultados.md`. Antes de entregar, verifica que los resultados coincidan con los obtenidos en tu equipo.

## 5. Revisar las actividades A2 y A3

- **A2:** abre `docs/matriz_A2.md` para consultar la comparación de modelos relacional, documental, clave-valor, familias de columnas y grafos.
- **A3:** abre `docs/consultas_A3.md` para revisar las consultas Q01–Q06, sus filtros y salidas, las reglas funcionales, las preguntas adicionales y el riesgo identificado.

## 6. Ejecutar la exploración A4 en MongoDB

Asegúrate de que el servidor MongoDB local esté ejecutándose y de estar en la carpeta raíz del proyecto. El comando utilizado en la práctica local sin credenciales fue:

```bash
mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" --file scripts/01_explorar.js
```

El script busca el documento `ASE-DEMO-001`; si no existe, lo inserta y luego muestra el documento, el conteo para ese identificador y la verificación del tipo `Date`. Su salida esperada incluye el conteo `1` y el valor `true` para `fecha_programada instanceof Date`.

La evidencia está registrada en `evidencias/A4/resultados.md` y los datos del entorno en `docs/entorno.md`.

**Limitación documentada:** la ejecución se realizó en una conexión local sin credenciales. Esto confirma conectividad y exploración, pero no acredita la conexión autenticada solicitada en la guía. Se debe verificar con la cuenta de práctica y la contraseña facilitadas por el instructor cuando estén disponibles. No se debe publicar ninguna contraseña en archivos ni en Git.

## 7. Lista de verificación para la entrega E01

- [ ] Revisar las respuestas teóricas y la autoevaluación de A1.
- [ ] Confirmar la ejecución de P1, P2 y P3 y conservar sus resultados.
- [ ] Revisar la matriz comparativa A2.
- [ ] Confirmar que A3 contiene Q01–Q06, reglas, dos preguntas y un riesgo.
- [ ] Revisar `docs/entorno.md` y `scripts/01_explorar.js`.
- [ ] Conservar evidencia de la ejecución de A4 sin contraseñas ni datos reales.
- [ ] Verificar la autenticación de A4 con las credenciales de práctica cuando el instructor las proporcione.
- [ ] Revisar `git status --short` antes de confirmar cambios y comprobar que no haya secretos incluidos.

## 8. Seguridad y control de versiones

No incluir contraseñas, URI con credenciales, archivos `.env`, respaldos con datos reales ni información personal. Si una credencial se publica accidentalmente en Git, ignorar el archivo después no elimina la exposición: se debe informar al responsable y rotar la credencial.
