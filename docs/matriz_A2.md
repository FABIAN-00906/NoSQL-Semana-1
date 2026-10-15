# A2 — Comparación de modelos NoSQL

## Objetivo

Comparar diferentes familias de bases de datos NoSQL según las necesidades del caso de la Unidad de Emprendimiento del SENA.

## Matriz de selección

| Caso | Modelo propuesto | Razón vinculada a una consulta | Límite o costo | Alternativa |
|---|---|---|---|---|
| Iniciativas de varios sectores | Documental (MongoDB) | Permite representar en un mismo documento los campos comunes de una iniciativa y atributos específicos según el sector, por ejemplo producto y canal de venta para alimentos o servicio digital y modalidad de entrega para software. | La flexibilidad de los documentos no elimina la necesidad de definir campos comunes y reglas claras; además, duplicar datos cambiantes puede generar problemas de coherencia. | SQL |
| Sesiones temporales | Clave-valor (Redis) | Permite recuperar rápidamente una sesión mediante una clave y manejar información temporal asociada al acceso al portal. | Los datos se organizan principalmente alrededor de una clave; no es la mejor opción si se necesitan relaciones complejas o consultas sobre múltiples atributos. | MongoDB |
| Recorridos de relaciones | Grafos (Neo4j) | Permite representar emprendedores, mentores y habilidades como nodos relacionados y consultar recorridos entre ellos. | Requiere un modelo orientado a relaciones y puede resultar innecesario si las consultas principales no necesitan recorrer conexiones complejas. | MongoDB |
| Lecturas por dispositivo/periodo | Familias de columnas (Cassandra) | Permite organizar grandes volúmenes de lecturas según particiones y consultas previstas por dispositivo y periodo. | Requiere diseñar cuidadosamente las particiones y las consultas previstas; no es la opción más conveniente para relaciones complejas entre entidades. | MongoDB |

## Situación en la que conservaría SQL

Conservaría SQL si la Unidad de Emprendimiento necesitara manejar información con relaciones estructuradas y reglas de integridad estrictas, por ejemplo, cuando sea fundamental garantizar que cada iniciativa tenga un emprendedor responsable existente y que las asesorías estén vinculadas correctamente a las iniciativas.

SQL sería especialmente conveniente si las consultas requirieran relaciones entre varias entidades y consistencia transaccional como requisito principal.

## Justificación

La selección del modelo depende de las necesidades de organización, acceso y crecimiento de los datos.

- **MongoDB** es adecuado para iniciativas con atributos variables según el sector.
- **Redis** es adecuado para datos temporales que se recuperan mediante una clave.
- **Neo4j** es adecuado cuando el problema requiere recorrer relaciones entre entidades.
- **Cassandra** es adecuado para grandes volúmenes de lecturas organizadas mediante particiones y consultas previstas.
- **SQL** continúa siendo una alternativa apropiada cuando se necesitan relaciones estructuradas, integridad y consistencia entre entidades.

La elección de una tecnología no debe basarse únicamente en su popularidad, sino en las consultas, relaciones, crecimiento y necesidades de coherencia del sistema.