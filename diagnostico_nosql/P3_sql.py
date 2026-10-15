import sqlite3

conexion = sqlite3.connect(":memory:")

conexion.executescript("""
CREATE TABLE emprendedores(
    id INTEGER PRIMARY KEY,
    alias TEXT
);

CREATE TABLE iniciativas(
    id INTEGER PRIMARY KEY,
    emprendedor_id INTEGER,
    estado TEXT
);

INSERT INTO emprendedores VALUES
(1, 'Emprendedor A'),
(2, 'Emprendedor B'),
(3, 'Emprendedor C');

INSERT INTO iniciativas VALUES
(101, 1, 'activa'),
(102, 2, 'archivada'),
(103, 1, 'activa');
""")

consulta = """
SELECT iniciativas.id, emprendedores.alias
FROM iniciativas
INNER JOIN emprendedores
    ON iniciativas.emprendedor_id = emprendedores.id
WHERE iniciativas.estado = 'activa'
ORDER BY iniciativas.id;
"""

print("=== INICIATIVAS ACTIVAS ===")

resultado = conexion.execute(consulta).fetchall()

for fila in resultado:
    print(fila)

conexion.close()