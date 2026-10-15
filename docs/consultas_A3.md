# A3 — Consultas y reglas de negocio

## Q01 — Iniciativas activas por sector y etapa didáctica

### Necesidad

Consultar las iniciativas que se encuentran activas, filtrando por sector y etapa didáctica.

- **Actor:** Responsable de la Unidad de Emprendimiento.
- **Filtros:** Estado de la iniciativa igual a `activa`, sector y etapa didáctica.
- **Campos de salida:** Código, nombre, sector, etapa didáctica y estado.
- **Orden:** Por código de iniciativa ascendente.
- **Frecuencia estimada:** Alta. Hipótesis de acceso frecuente para realizar seguimiento de las iniciativas.

**Resultado esperado:** Lista de iniciativas activas que cumplan los filtros de sector y etapa didáctica. Si no existen coincidencias, se devuelve una lista vacía.

## Q02 — Detalle de una iniciativa

### Necesidad

Consultar el detalle de una iniciativa específica, incluyendo su propuesta de valor y los atributos particulares de su sector.

- **Actor:** Responsable de la Unidad de Emprendimiento.
- **Filtros:** Código de la iniciativa.
- **Campos de salida:** Código, nombre, propuesta de valor, sector y atributos específicos.
- **Orden:** No aplica para una consulta de una iniciativa individual.
- **Frecuencia estimada:** Alta. Hipótesis de consulta durante las asesorías.

## Q03 — Iniciativas de un emprendedor responsable por estado

### Necesidad

Consultar las iniciativas asociadas a un emprendedor responsable y filtrarlas por estado.

- **Actor:** Responsable de la Unidad de Emprendimiento.
- **Filtros:** Código del emprendedor responsable y estado de la iniciativa.
- **Campos de salida:** Código de iniciativa, nombre, sector, etapa didáctica y estado.
- **Orden:** Por código de iniciativa ascendente.
- **Frecuencia estimada:** Media. Hipótesis de consulta durante el seguimiento.

**Resultado esperado:** Lista de iniciativas pertenecientes al emprendedor indicado que cumplan el estado solicitado.

## Q04 — Asesorías programadas pendientes

### Necesidad

Consultar las asesorías programadas que están pendientes dentro de un rango de fechas y según la modalidad.

- **Actor:** Responsable de la Unidad de Emprendimiento.
- **Filtros:** Estado igual a `programada`, rango de fechas de la fecha programada y modalidad.
- **Campos de salida:** Código de asesoría, código o nombre de iniciativa, código del asesor, fecha programada y modalidad.
- **Orden:** Por fecha programada ascendente.
- **Frecuencia estimada:** Alta. Hipótesis de consulta para organizar la agenda.

**Resultado esperado:** Lista de asesorías programadas que cumplen el rango de fechas y la modalidad indicada, ordenadas desde la fecha más próxima.

## Q05 — Historial de asesorías de una iniciativa

### Necesidad

Consultar el historial de asesorías asociadas a una iniciativa.

- **Actor:** Responsable de la Unidad de Emprendimiento.
- **Filtros:** Código de la iniciativa.
- **Campos de salida:** Código de asesoría, estado, modalidad, fecha programada, fecha de realización y temas.
- **Orden:** Por fecha programada ascendente.
- **Frecuencia estimada:** Media. Hipótesis de consulta para realizar seguimiento de la iniciativa.

**Resultado esperado:** Historial de las asesorías relacionadas con la iniciativa, incluyendo las programadas, realizadas y canceladas.

## Q06 — Cantidad de asesorías realizadas por sector y mes

### Necesidad

Consultar la cantidad de asesorías realizadas, agrupadas por sector de la iniciativa y por mes.

- **Actor:** Responsable de la Unidad de Emprendimiento.
- **Filtros:** Estado igual a `realizada` y rango de fechas de realización.
- **Campos de salida:** Sector, mes y cantidad de asesorías.
- **Orden:** Por mes ascendente y, dentro de cada mes, por sector ascendente.
- **Frecuencia estimada:** Baja. Hipótesis de consulta para análisis periódico.

### Decisión sobre el sector

Para esta consulta se utilizará inicialmente el sector actual de la iniciativa. En el modelado posterior se deberá evaluar si es necesario conservar también el sector correspondiente al momento de la asesoría para mantener correctamente el historial.

La agrupación mensual se realizará utilizando la fecha de realización de cada asesoría, no la fecha programada.

## Reglas de negocio

### Reglas funcionales

1. Los códigos de emprendedores deben ser únicos.
2. Los códigos de iniciativas deben ser únicos.
3. Los códigos de asesorías deben ser únicos.
4. Cada iniciativa debe tener un emprendedor responsable existente.
5. Un mismo emprendedor puede tener varias iniciativas.
6. Cada asesoría debe estar asociada a una iniciativa existente.
7. Cada asesoría debe registrar el código ficticio del asesor que la atiende.
8. Los sectores permitidos para las iniciativas son:
   - `tecnologia`
   - `alimentos`
   - `economia_circular`
9. Las etapas didácticas permitidas son:
   - `idea`
   - `validacion`
   - `puesta_en_marcha`
10. Los estados permitidos para una iniciativa son:
    - `activa`
    - `archivada`
11. Los estados permitidos para una asesoría son:
    - `programada`
    - `realizada`
    - `cancelada`
12. Toda asesoría debe registrar `fecha_programada`.
13. Cuando una asesoría sea realizada, debe registrar `fecha_realizacion`.
14. La `fecha_realizacion` puede ser diferente de la `fecha_programada`. Una reprogramación no debe modificar la fecha anterior de forma que se pierda u oculte el historial del cambio.
15. No deben existir dos asesorías del mismo asesor en franjas horarias superpuestas. Para este ejercicio se supone una duración de 60 minutos por asesoría. Por tanto, una asesoría de 08:00 a 09:00 entra en conflicto con otra de 08:30 a 09:30 para el mismo asesor. Esta duración es un supuesto didáctico y debe ajustarse si el instructor define otra. La validación y el control de solicitudes simultáneas se implementarán posteriormente.
16. Archivar una iniciativa no debe eliminar su historial de asesorías.

### Mecanismos de implementación

Las reglas anteriores representan requisitos funcionales del negocio. La validación mediante índices únicos, validaciones de documentos, controles de fechas y mecanismos para gestionar solicitudes simultáneas se definirá posteriormente durante el diseño y la implementación de la base de datos.

## Preguntas adicionales

### Pregunta 1

¿Qué información adicional debería registrar la Unidad de Emprendimiento para evaluar el avance de una iniciativa?

### Pregunta 2

¿Qué información debería conservarse de una asesoría para facilitar el seguimiento posterior de la iniciativa?

## Riesgo identificado

Un riesgo es que existan inconsistencias entre la información de las iniciativas y las asesorías. Por ejemplo, una asesoría podría quedar asociada a una iniciativa inexistente, o una modificación de la fecha programada podría hacer que se pierda el historial de una reprogramación.

Para reducir este riesgo, se deberán definir mecanismos de validación de referencias y conservación del historial durante el diseño e implementación de la base de datos.
