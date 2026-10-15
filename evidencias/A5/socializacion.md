# A5 — Socialización y nivelación

## 1. Selección del modelo de datos

Se propone utilizar el modelo documental de MongoDB para el caso de la Unidad de Emprendimiento, debido a que las iniciativas pueden tener atributos específicos según su sector. Esta elección requiere definir reglas claras para los campos comunes y mantener la coherencia de la información.

## 2. Consulta seleccionada

**Q03 — Iniciativas de un emprendedor responsable por estado.**

Esta consulta permite localizar las iniciativas asociadas a un emprendedor específico y filtrarlas según su estado. Devuelve el código, nombre, sector, etapa didáctica y estado de cada iniciativa encontrada.

## 3. Tipo de dato identificado

**Date en MongoDB.**

En la práctica de A4 se verificó que el campo `fecha_programada` del documento `ASE-DEMO-001` corresponde a un valor de tipo fecha mediante la expresión `instanceof Date`, cuyo resultado fue `true`.

## 4. Dificultad encontrada

Se logró realizar una conexión local a MongoDB sin credenciales y ejecutar el script de exploración. Sin embargo, no se pudo comprobar la conexión autenticada porque no se proporcionaron las credenciales de la cuenta de práctica.

## 5. Retroalimentación de la socialización

- **Observaciones del instructor o compañero:** Pendiente de registrar.
- **Fortalezas identificadas:** Pendiente de confirmar durante la socialización.
- **Aspectos por mejorar:** Pendiente de acordar.

## 6. Acción de mejora

- **Acción acordada:** Pendiente de acordar con el instructor.
- **Fecha acordada:** Pendiente de definir.
- **Seguimiento:** Registrar el resultado una vez realizada la acción.

**Nota:** Esta evidencia se prepara antes de la socialización. Las observaciones, los acuerdos y la fecha deben completarse con la retroalimentación real recibida.
