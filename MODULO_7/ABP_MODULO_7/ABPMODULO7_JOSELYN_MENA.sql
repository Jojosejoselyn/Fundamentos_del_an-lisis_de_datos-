-- PROYECTO ABP MÓDULO 7 -- Sistema de gestión de ventas --
-- LIMPIAR TODO 
DROP TABLE IF EXISTS Ventas;
DROP TABLE IF EXISTS Productos;
DROP TABLE IF EXISTS Clientes;


-- CREAR CLIENTES
CREATE TABLE Clientes (
    cliente_id INTEGER PRIMARY KEY,
    nombres TEXT NOT NULL,
    ciudad TEXT,
    region TEXT,
    genero TEXT,
    telefono TEXT,
    email TEXT,
    fecha_registro DATE
);

INSERT INTO Clientes VALUES
(1, 'Ana Torres', 'Santiago', 'RM', 'F', '123456789', 'ana@mail.com', '2026-01-10'),
(2, 'Luis Rojas', 'Valparaíso', 'V', 'M', '987654321', 'luis@mail.com', '2026-01-15'),
(3, 'Camila Pérez', 'Concepción', 'VIII', 'F', '456123789', 'camila@mail.com', '2026-01-20');


-- CREAR PRODUCTOS
CREATE TABLE Productos (
    producto_id INTEGER PRIMARY KEY,
    nombre_producto TEXT NOT NULL,
    categoria TEXT,
    precio_unitario REAL,
    fecha_ingreso DATE
);

INSERT INTO Productos VALUES
(1, 'Notebook', 'Tecnologia', 800000, '2026-01-01'),
(2, 'Mouse', 'Accesorios', 15000, '2026-01-05'),
(3, 'Teclado', 'Accesorios', 30000, '2026-01-10');


-- CREAR VENTAS
CREATE TABLE Ventas (
    venta_id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    producto_id INTEGER,
    fecha DATE,
    cantidad INTEGER,
    total_venta REAL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id),
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id)
);

INSERT INTO Ventas VALUES
(1, 1, 1, '2026-02-01', 1, 800000),
(2, 1, 2, '2026-02-05', 2, 30000),
(3, 2, 3, '2026-02-10', 1, 30000);


-- CONSULTA JOIN
SELECT c.nombres, p.nombre_producto, v.fecha, v.total_venta
FROM Ventas v
JOIN Clientes c ON c.cliente_id = v.cliente_id
JOIN Productos p ON p.producto_id = v.producto_id;

-- Total general de ventas
SELECT 
    COUNT(*) AS numero_ventas,
    SUM(total_venta) AS total_vendido,
    ROUND(SUM(total_venta) / COUNT(*), 2) AS promedio
FROM Ventas;

-- Total gastado por cada cliente
SELECT 
    c.nombres,
    SUM(v.total_venta) AS total_gastado
FROM Ventas v
JOIN Clientes c ON c.cliente_id = v.cliente_id
GROUP BY c.nombres;

-- Total vendido por producto
SELECT 
    p.nombre_producto,
    SUM(v.total_venta) AS total_vendido
FROM Ventas v
JOIN Productos p ON p.producto_id = v.producto_id
GROUP BY p.nombre_producto;

-- Clientes que han comprado más de una vez
SELECT nombres
FROM Clientes
WHERE cliente_id IN (
    SELECT cliente_id
    FROM Ventas
    GROUP BY cliente_id
    HAVING COUNT(*) > 1
);

-- Producto más vendido
SELECT nombre_producto
FROM Productos
WHERE producto_id IN (
    SELECT producto_id
    FROM Ventas
    GROUP BY producto_id
    ORDER BY SUM(cantidad) DESC
    LIMIT 1
);

-- Cliente que más gastó
SELECT c.nombres, SUM(v.total_venta) AS total
FROM Ventas v
JOIN Clientes c ON c.cliente_id = v.cliente_id
GROUP BY c.nombres
HAVING total = (
    SELECT MAX(total_cliente)
    FROM (
        SELECT SUM(total_venta) AS total_cliente
        FROM Ventas
        GROUP BY cliente_id
    )
);

-- Agregar columna stock
ALTER TABLE Productos
ADD COLUMN stock INTEGER;

-- Inicializar stock
UPDATE Productos
SET stock = 10;

-- Restar stock (ejemplo producto 1)
UPDATE Productos
SET stock = stock - 1
WHERE producto_id = 1;

-- Eliminar producto obsoleto
DELETE FROM Productos
WHERE producto_id = 3;

-- Ver estado final de productos
SELECT * FROM Productos;